import cv2
import numpy as np
import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk

import image_loader


def on_shape_selected(event):
    global selected_shape
    # This way we store the shape we have selected in a variable: selected_shape
    selected_shape = shape_combobox.get()
    print(f"Selected shape: {selected_shape}")
    set_image_displayed(draw_shape(selected_shape))


def set_image_displayed(img):
    global img_tk

    # Convert the image to the correct format
    image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Create a Tkinter PhotoImage object
    img = Image.fromarray(image)
    img_tk = ImageTk.PhotoImage(image=img)

    # Create a Tkinter Canvas widget
    canvas = tk.Canvas(root, width=img.width, height=img.height)
    canvas.create_image(0, 0, anchor="nw", image=img_tk)
    canvas.grid(row=1, column=0)


def draw_shape(shape):
    img = input_image.copy()
    center = (img.shape[1] // 2, img.shape[0] // 2)
    color = (0, 255, 0)

    # We can replace these img = ... with the call to the function that will recreate the image using a specific shape
    if shape == "Circle":
        img = cv2.circle(img, center, 10, color, 2)
    elif shape == "Rectangle":
        img = cv2.rectangle(img, (10, 10), (30, 30), color, 2)
    elif shape == "Triangle":
        pts = np.array([[10, 30], [30, 30], [20, 10]], dtype=np.int32)
        img = cv2.polylines(img, [pts], True, color, 2)
    elif shape == "Ellipse":
        img = cv2.ellipse(img, center, (15, 10), 0, 0, 360, color, 2)

    return img


# I think about sticking to these figures for now
shapes = ["Triangle", "Circle", "Rectangle", "Ellipse"]

selected_shape = None
shape_combobox = None
root = None
input_image = None


def start_gui(input_image_file_name: str):
    global shape_combobox, root, input_image

    input_image = image_loader.load_image(input_image_file_name)

    # Creating the small window where we can select the shape:
    root = tk.Tk()
    root.title("Primitive Shape Selector")

    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))  # sticky makes the text stretch in all directions

    shape_label = ttk.Label(frame, text="Choose a primitive shape:")
    shape_label.grid(row=0, column=0, padx=(0, 10), pady=(0, 10), sticky=tk.W)

    shape_combobox = ttk.Combobox(frame, values=shapes)
    shape_combobox.grid(row=0, column=1, pady=(0, 10))
    shape_combobox.bind("<<ComboboxSelected>>", on_shape_selected)

    # Optional as fuck
    ttk.Button(frame, text="Quit", command=root.destroy).grid(column=1, row=1)

    set_image_displayed(input_image)

    root.mainloop()
