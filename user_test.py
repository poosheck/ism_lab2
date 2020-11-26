import glob
import random
import json
from tkinter import *

import cv2
from PIL import Image
from PIL import ImageTk

IMG = None
gray = None
results = []

def operate_image(filename):
    global panelA, gray, IMG, results
    im = Image.open(filename)
    IMG = cv2.imread(filename)

    IMG = cv2.cvtColor(IMG, cv2.COLOR_BGR2GRAY)

    scale_percent = 100  # percent of original size
    width = int(IMG.shape[1] * scale_percent / 100)
    height = int(IMG.shape[0] * scale_percent / 100)
    dim = (width, height)

    IMG = cv2.resize(IMG, dim, interpolation=cv2.INTER_AREA)

    image = Image.fromarray(IMG)
    image = ImageTk.PhotoImage(image)

    if panelA is None:
        panelA = Label(image=image)
        panelA.image = image
        panelA.grid(row=1, column=0, padx=10, pady=10)
    else:
        panelA.configure(image=image)
        panelA.image = image

    score = IntVar()
    waiter = IntVar()
    score.set(0)

    bottomframe = Frame(root)
    bottomframe.grid(row=2, column=0, columnspan=6)
    btn_1 = Button(bottomframe, text="1", command=lambda : score.set(1))
    btn_1.grid(row=0, column=0)
    btn_2 = Button(bottomframe, text="2", command=lambda : score.set(2))
    btn_2.grid(row=0, column=1)
    btn_3 = Button(bottomframe, text="3", command=lambda : score.set(3))
    btn_3.grid(row=0, column=2)
    btn_4 = Button(bottomframe, text="4", command=lambda : score.set(4))
    btn_4.grid(row=0, column=3)
    btn_5 = Button(bottomframe, text="5", command=lambda : score.set(5))
    btn_5.grid(row=0, column=4)
    btn_wait = Button(bottomframe, text="next", command=lambda : waiter.set(1))
    btn_wait.grid(row=0,column=5)

    btn_wait.wait_variable(waiter)
    results.append({
        'filename': filename,
        'score': score.get()
    })

    if (score.get() != 0):
        bottomframe.destroy()
        return score


def run():
    topframe.destroy()
    global panelA, gray, IMG
    filename = 'original_image.jpg'
    if len(filename) > 0:
        operate_image(filename)

    file_list = []
    for name in glob.glob('./compressed_*.jpg'):
        file_list.append(name)

    random.shuffle(file_list)

    for file in file_list:
        operate_image(file)

    panelA.destroy()

    with open('results.json','w') as f:
        json.dump(results, f, indent=2)

    Label_1 = Label(root, text="Please send results.json file back to me :)")
    Label_1.pack()
    Label_2 = Label(root, text="You can now close this window")
    Label_2.pack()



if __name__ == "__main__":
    root = Tk()
    #  root.attributes("-fullscreen", True)
    panelA = None

    topframe = Frame(root)
    topframe.grid(row=5, column=0, columnspan=2)

    Label_1 = Label(topframe, text="Please mark your score based on how good you think the image looks").grid(row=0, column=0)
    Label_2 = Label(topframe, text="After an image is shown - press one of the score buttons (1-5) and confirm with Next button").grid(row=1, column=0)
    Label_2 = Label(topframe, text="First image is uncompressed, original image.").grid(row=2, column=0)
    Label_3 = Label(topframe, text="Press Start to start").grid(row=3, column=0)

    btn = Button(topframe, text="Start", command=run).grid(row=4, column=0)
    exit_btn = Button(topframe, text="Exit", command=root.destroy).grid(row=4, column=1)


    root.mainloop()