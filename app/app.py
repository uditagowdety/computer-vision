import tkinter as tk
from PIL import Image, ImageTk

def button_Clicked():
    label.config(text="button was clicked lol")

root=tk.Tk()
root.title("trying")
root.geometry("1000x600")

path1=r"C:\Users\student\PycharmProjects\220962410_Udita\flower.jpg"
path2=r"C:\Users\student\PycharmProjects\220962410_Udita\neg_flower.jpg"

image1=Image.open(path1)
image2=Image.open(path2)

# label=tk.Label(root,text="uhhhhh")
# label.pack(pady=10)
#
# button=tk.Button(root, text="dont click me aha",command=button_Clicked)
# button.pack(pady=10)

photo_original=ImageTk.PhotoImage(image1)
photo_neg=ImageTk.PhotoImage(image2)

label_original=tk.Label(root, image=photo_original)
label_neg=tk.Label(root, image=photo_neg)

label_original.grid(row=0,column=0,padx=10,pady=100)
label_neg.grid(row=0,column=1,padx=10,pady=100)

root.mainloop()