import tkinter
import os
import tkinter.ttk
from PIL import ImageTk,Image
from tkinter import messagebox


def on_exit():
    messagebox.showinfo(None,"Thanks for using my program")
    root.destroy()

def launch_script_cmd():
    selected_script = combo_box_text.get()
    print(selected_script)
    if selected_script =="Image Compressor":
        os.system("python scripts/Compressor.py")
    elif selected_script =="Temp File Deleter":
        os.system("python scripts/Deleter.py")
    elif selected_script =="Speed Test":
        os.system("python scripts/Speed.py")
    pass
root = tkinter.Tk()
root.protocol("WM_DELETE_WINDOW",on_exit)
root.title("Blake's MultiTool")
root.geometry("500x300")
background_image=ImageTk.PhotoImage(Image.open("assets\\background.png"))
image_panel=tkinter.Label(root,image=background_image)
image_panel.pack(fill="both",expand="yes")

title_label = tkinter.Label( image_panel,text="Blake's MultiTool",foreground="blue",font=("Segoe UI Light",16))
title_label.pack()

combo_box_text = tkinter.StringVar()
combo_box = tkinter.ttk.Combobox(image_panel,textvariable=combo_box_text,state="readonly")
combo_box["values"] = ["Image Compressor","Temp File Deleter","Speed Test"]
combo_box.pack()

launch_button = tkinter.Button(image_panel,text="launch",command=launch_script_cmd)
launch_button.pack()
root.iconbitmap("assets\\image.ico")
root.mainloop()