import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root=tk.Tk()
root.title("trying")
root.geometry("1000x800")

label = tk.Label(root)
label.pack(expand=True)

images={
    "original":ImageTk.PhotoImage(Image.open(r"C:\Users\student\PycharmProjects\220962410_Udita\images\flower.jpg")),
    "negative":ImageTk.PhotoImage(Image.open(r"C:\Users\student\PycharmProjects\220962410_Udita\images\neg_flower.jpg")),
    "gamma":ImageTk.PhotoImage(Image.open(r"C:\Users\student\PycharmProjects\220962410_Udita\images\gamma_flower.jpg"))
}

titles={
    "original":"original image",
    "negative":"negative image",
    "gamma":"gamma image"
}

main_frame = tk.Frame(root)
main_frame.pack(expand=True, fill='both')

image_frame = tk.Frame(main_frame)
image_frame.pack(side=tk.TOP, padx=10, pady=10, fill='both', expand=True)

combobox_frame = tk.Frame(main_frame)
combobox_frame.pack(side=tk.BOTTOM, padx=10, pady=10, fill='x')

frame1 = tk.Frame(image_frame)
frame1.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

frame2 = tk.Frame(image_frame)
frame2.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

original_image_label = tk.Label(frame1, image=images["original"])
original_title_label = tk.Label(frame1, text=titles["original"], font=("Arial", 12))
original_image_label.pack(expand=True)
original_title_label.pack()

dynamic_image_label = tk.Label(frame2) #???
dynamic_title_label = tk.Label(frame2, font=("Arial", 12))
dynamic_image_label.pack(expand=True)
dynamic_title_label.pack()

combobox_frame = tk.Frame(combobox_frame)
combobox_frame.pack(side=tk.BOTTOM, padx=10, pady=10, fill=tk.X)

combobox=ttk.Combobox(combobox_frame, values=list(images.keys()))
combobox.pack()

def update_image(event):
    selected_image = combobox.get()
    new_image = images[selected_image]
    new_title = titles[selected_image]
    dynamic_image_label.config(image=new_image)
    dynamic_title_label.config(text=new_title)

combobox.bind("<<ComboboxSelected>>", update_image)

# Set initial image
dynamic_image_label.config(image=images["negative"])
dynamic_title_label.config(text=titles["negative"])

root.mainloop()