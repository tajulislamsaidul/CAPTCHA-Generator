import tkinter as tk
from tkinter import messagebox
from captcha.image import ImageCaptcha
from PIL import Image, ImageTk
import random
import string
import os

def generate_captcha(text):
    image = ImageCaptcha(width=300, height=100)
    filename = "captcha_gui.png"
    image.write(text, filename)
    return filename

def show_image(filepath):
    image = Image.open(filepath)
    image = image.resize((300, 100))
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.image = photo

def create_and_show():
    text = entry.get()
    if not text:
        messagebox.showwarning("Input Needed", "Please enter CAPTCHA text.")
        return
    filename = generate_captcha(text)
    show_image(filename)

def generate_random_text():
    text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    entry.delete(0, tk.END)
    entry.insert(0, text)
    filename = generate_captcha(text)
    show_image(filename)

root = tk.Tk()
root.title("CAPTCHA Generator")
root.geometry("350x300")

tk.Label(root, text="Enter CAPTCHA Text or Generate Random:").pack(pady=10)
entry = tk.Entry(root, font=("Arial", 14), width=20)
entry.pack()

tk.Button(root, text="Generate CAPTCHA", command=create_and_show).pack(pady=5)
tk.Button(root, text="Random CAPTCHA", command=generate_random_text).pack(pady=5)

image_label = tk.Label(root)
image_label.pack(pady=10)

root.mainloop()