from tkinter import *
from tkinter import filedialog

from PIL import Image

IMG=None
gray=None

def compress(image):
    image.save("original_image.jpg","JPEG", optimize = True, quality=100)
    image.save("compressed_10.jpg","JPEG", optimize = True, quality=10)
    image.save("compressed_20.jpg","JPEG", optimize = True, quality=20)
    image.save("compressed_30.jpg","JPEG", optimize = True, quality=30)
    image.save("compressed_40.jpg","JPEG", optimize = True, quality=40)
    image.save("compressed_50.jpg","JPEG", optimize = True, quality=50)
    image.save("compressed_60.jpg","JPEG", optimize = True, quality=60)
    image.save("compressed_70.jpg","JPEG", optimize = True, quality=70)
    image.save("compressed_80.jpg","JPEG", optimize = True, quality=80)
    image.save("compressed_90.jpg","JPEG", optimize = True, quality=90)
    image.save("compressed_99.jpg","JPEG", optimize = True, quality=99)
    print("Saved new files, can exit.")

def select_image():
    global panelA, gray, IMG
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetype = (("jpeg files", "*.jpg"),("all files", "*.*")))
    print(filename)
    if len(filename) > 0:
        im = Image.open(filename)
        compress(im)


if __name__ == "__main__":
    root = Tk()
    panelA = None

    topframe = Frame(root)
    topframe.grid(row=0, column=0, columnspan=3)

    btn = Button(topframe, text="Select an image for compression", command=select_image).grid(row=0, column=0)
    exit_btn = Button(topframe, text="Exit", command=root.destroy).grid(row=0, column=2)

    root.mainloop()