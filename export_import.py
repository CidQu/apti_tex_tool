import io
import os
from binary_reader import BinaryReader
from cv2 import exp

apti_tex_magic = bytes.fromhex('6D 32 F3 C3')
DDS_Header = b'DDS |\x00\x00\x00\x07\x10\x08\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x01\x00\x00\x00GIMP-DDS\\\t\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x04\x00\x00\x00DXT5\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
apti_tex_header = b'm2\xf3\xc3\xd1\x9ce\xe9\x9a\xbc\x0f\r"\xdb\xdaO\x00Q5!k\xc7\xd8\x01;\x00\x04\x007\x00\x00\x00\x04\x00\x04\x00\x0c\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9a\xbc\x0f\r"\xdb\xdaO\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x04\x00\xc5\x04\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1d\x02\x00\x00\x00\x00\xff\x00'
zeros = b'\x00'*4

def export_command(file_path, dirname):
    try:
        file_name = os.path.basename(file_path)
        outputfile = dirname + '\\' + file_name[:-9] + '.DDS'
        file_stats = os.stat(file_path)
        f = open(file_path, "rb")

        reader = BinaryReader(f.read())

        if reader.read_bytes(4) != b'\x6d\x32\xf3\xc3':
            raise IOError("Error: %s This file is not *.apti_tex file.")
        else:
            with open(outputfile, 'wb') as out_file:
                reader.seek(105)
                dosya = reader.read_bytes(file_stats.st_size-105)
                out_file.write(DDS_Header + dosya)
                out_file.seek(-4, io.SEEK_END)
                out_file.truncate()
            return 'Done!'
    except:
        return 'Something went wrong.'

def import_command(file_path, dirname):
    try:
        file_name = os.path.basename(file_path)
        outputfile = dirname + '\\' + file_name[:-4] + '.APTI_TEX'
        file_stats = os.stat(file_path)
        f = open(file_path, "rb")

        reader = BinaryReader(f.read())

        if reader.read_bytes(130) != DDS_Header:
            raise IOError("Error: %s This file is not proper *.dds file.")
        else:
            with open(outputfile, 'wb') as out_file:
                reader.seek(130)
                dosya = reader.read_bytes(file_stats.st_size-130)

                reader_for_dds = BinaryReader(dosya)

                reader_for_dds.seek(4, whence=2)
                reader_for_dds.write_bytes(zeros)
                reader_for_dds.seek(0)
                size_dosya = reader_for_dds.size()

                out_file.write(apti_tex_header + reader_for_dds.read_bytes(size_dosya) + zeros)
            return 'Done!'
    except:
        return 'Something went wrong'
