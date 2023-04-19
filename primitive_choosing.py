import cv2
import numpy as np
import tkinter as tk
from tkinter import ttk


def on_shape_selected(event):
    global selected_shape
    # This way we store the shape we have selected in a variable: selected_shape
    selected_shape = shape_combobox.get()
    print(f"Selected shape: {selected_shape}")
    draw_shape(selected_shape)


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

    # Display the image with the drawn shape
    cv2.imshow("Shape", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Read the input image
input_image = cv2.imread("ex0.png")

# I think about sticking to these figures for now
shapes = ["Triangle", "Circle", "Rectangle", "Ellipse"]

selected_shape = None

# Creating the small window where we can select the shape:
root = tk.Tk()
root.title("Primitive Shape Selector")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S)) # sticky makes the text stretch in all directions

shape_label = ttk.Label(frame, text="Choose a primitive shape:")
shape_label.grid(row=0, column=0, padx=(0, 10), pady=(0, 10), sticky=tk.W)

shape_combobox = ttk.Combobox(frame, values=shapes)
shape_combobox.grid(row=0, column=1, pady=(0, 10))
shape_combobox.bind("<<ComboboxSelected>>", on_shape_selected)

# Optional as fuck
ttk.Button(frame, text="Quit", command=root.destroy).grid(column=1, row=1)

root.mainloop()
