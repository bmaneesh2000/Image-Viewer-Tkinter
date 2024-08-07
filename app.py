import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image, ImageTk
import os

def load_images():
    global image_paths, current_image_index
    folder_path = filedialog.askdirectory(title="Select Folder")
    if not folder_path:
        status.config(text="No folder selected")
        return

    image_paths = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    if image_paths:
        current_image_index = 0
        show_image(current_image_index)
        status.config(text=f"Displaying image {current_image_index + 1} of {len(image_paths)}")
    else:
        status.config(text="No images found in the selected folder")

def show_image(index):
    global tk_image
    if 0 <= index < len(image_paths):
        image_path = image_paths[index]
        image = Image.open(image_path)
        image = image.resize((800, 600), Image.LANCZOS)
        tk_image = ImageTk.PhotoImage(image)

        canvas.delete("all")
        canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)
        status.config(text=f"Displaying image {index + 1} of {len(image_paths)}")

def show_prev_image():
    global current_image_index
    if image_paths:
        current_image_index = (current_image_index - 1) % len(image_paths)
        show_image(current_image_index)

def show_next_image():
    global current_image_index
    if image_paths:
        current_image_index = (current_image_index + 1) % len(image_paths)
        show_image(current_image_index)

# Main Tkinter window
root = tk.Tk()
root.title("Image Viewer")
root.geometry("800x600")
root.configure(bg="black")

canvas = tk.Canvas(root, bg="#000080")
canvas.pack(fill=tk.BOTH, expand=True)

button_frame = tk.Frame(root, bg="black")
button_frame.pack(side=tk.BOTTOM, fill=tk.X)

style = ttk.Style()
style.configure("TButton", font=("Helvetica", 10), padding=10)

prev_button = ttk.Button(button_frame, text="Previous", command=show_prev_image)
prev_button.pack(side=tk.LEFT, padx=20, pady=10)

next_button = ttk.Button(button_frame, text="Next", command=show_next_image)
next_button.pack(side=tk.RIGHT, padx=20, pady=10)

status = tk.Label(root, text="Select a folder to view images", bd=1, relief=tk.SUNKEN, anchor=tk.W, bg="black", fg="white")
status.pack(side=tk.BOTTOM, fill=tk.X)

image_paths = []
current_image_index = 0

# Load images initially
load_images()

root.mainloop()
