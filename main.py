import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog
import io
import os
import csv
from binary_reader import BinaryReader

apti_tex_magic = bytes.fromhex('6D 32 F3 C3')
DDS_Header = b'DDS |\x00\x00\x00\x07\x10\x08\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x01\x00\x00\x00GIMP-DDS\\\t\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x04\x00\x00\x00DXT5\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

class App:
    

    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_888=tk.Label(root)
        ft = tkFont.Font(family='Times',size=22)
        GLabel_888["font"] = ft
        GLabel_888["fg"] = "#333333"
        GLabel_888["justify"] = "center"
        GLabel_888["text"] = "*.apti_tex Exporter and Importer"
        GLabel_888.place(x=100,y=20,width=401,height=35)

        GLabel_62=tk.Label(root)
        ft = tkFont.Font(family='Times',size=15)
        GLabel_62["font"] = ft
        GLabel_62["fg"] = "#333333"
        GLabel_62["justify"] = "center"
        GLabel_62["text"] = "Made by CidQu"
        GLabel_62.place(x=230,y=60,width=130,height=30)

        export_button=tk.Button(root)
        export_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        export_button["font"] = ft
        export_button["fg"] = "#000000"
        export_button["justify"] = "center"
        export_button["text"] = "Export!"
        export_button.place(x=40,y=160,width=159,height=52)
        export_button["command"] = self.export_button_command

        import_button=tk.Button(root)
        import_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        import_button["font"] = ft
        import_button["fg"] = "#000000"
        import_button["justify"] = "center"
        import_button["text"] = "Import"
        import_button.place(x=380,y=160,width=160,height=53)
        import_button["command"] = self.import_button_command

        GLabel_333=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        GLabel_333["font"] = ft
        GLabel_333["fg"] = "#333333"
        GLabel_333["justify"] = "center"
        GLabel_333["text"] = "After export, you  will recieve a *.dds file\nyou can edit this file using GIMP. \nYou need to edit this *.dds in BC3/DXT5. \nThen you can import back. \nFor more, please open an issue on  Github/apti_tex_editor"
        GLabel_333.place(x=0,y=280,width=600,height=120)

    def export_button_command(self):
        file_path = filedialog.askopenfilename()
        dirname = filedialog.askdirectory()
        file_name = os.path.basename(file_path)
        outputfile = dirname + '\\' + file_name + '.DDS'
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
                print('bitti1')
                out_file.seek(-4, io.SEEK_END)
                out_file.truncate()

            


    def import_button_command(self):
        file_path = filedialog.askopenfilename()
        dirname = filedialog.askdirectory()
        file_name = os.path.basename(file_path)
        outputfile = dirname + '\\' + file_name + '.APTI_TEX'
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
                print('bitti1')
                out_file.seek(-4, io.SEEK_END)
                out_file.truncate()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
