import PIL
from PIL import Image
from tkinter.filedialog import *
import customtkinter
import ctypes
from tkinter import *
from tkinter import messagebox

def Compressed():

    file_path=askopenfilename()
    try:
        img=PIL.Image.open(file_path)
        myHeight,myWidth=img.size
        save_path=asksaveasfilename()
        img.save(save_path+"compressed.jpg")
        messagebox.showinfo("Successfully Compressed","Successfully Compressed")
    except Exception as ex:
        print(ex)
        print("error")

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x300")

root.iconbitmap("C:\\Users\\Kmuwl\\Downloads\\Tatice-Operating-Systems-Apple-Blue.256.ico")

root.title("Blake's Compressor")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=50, fill="both", expand=True)
img = customtkinter.CTkCanvas(frame,)
img.pack(fill = "both",expand = True)
photo = PhotoImage(file = "assets/background.PNG")

img.create_image(0,0,anchor = "nw",image = photo)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Compressed")

button = customtkinter.CTkButton(master=frame, text="Compressed", command=Compressed)
button.pack(pady=12, padx=10)

button.place(relx = 0.5, rely = 0.5, anchor = customtkinter.CENTER)

root.mainloop()
