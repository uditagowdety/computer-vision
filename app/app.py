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

frame1 = tk.Frame(root)
frame2 = tk.Frame(root)

frame1.grid(row=0,column=0,padx=10,pady=100, sticky="nsew")
frame2.grid(row=0,column=1,padx=10,pady=100, sticky="nsew")

title1 = tk.Label(frame1, text="original image", font=("Arial", 12))
title2 = tk.Label(frame2, text="negative image", font=("Arial", 12))

label1=tk.Label(frame1, image=photo_original)
label2=tk.Label(frame2, image=photo_neg)

title1.pack()
label1.pack(expand=True)
title2.pack()
label2.pack(expand=True)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

root.mainloop()