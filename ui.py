import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog
import export_import

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
        cevap = export_import.export_command(file_path=file_path, dirname=dirname)
        print(cevap)

    def import_button_command(self):
        file_path = filedialog.askopenfilename()
        dirname = filedialog.askdirectory()
        cevap = export_import.import_command(file_path=file_path, dirname=dirname)
        print(cevap)

root = tk.Tk()
app = App(root)
root.mainloop()
