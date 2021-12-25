import datetime
from tkinter import *
from tkinter import filedialog
import os
from PIL import Image

window = Tk()
window.title("Upload Photo to watermark...")
window.config(padx=50, pady=50)

def open_img_file():
    global image
    filename = filedialog.askopenfilename(initialdir=os.getcwd(
    ), title="Select file")

    outfile = datetime.datetime.now().isoformat() + ".jpg"
    if not filename:
        return

    with Image.open(filename) as img:
        width, height = img.size

        with Image.open("hqdefault.jpeg") as wm:
            rgb_im = img.convert('RGB')
            wm.putalpha(200)
            transparent = Image.new('RGBA', (width, height), (0, 0, 0, 0))
            transparent.paste(rgb_im, (0, 0))
            transparent.paste(wm, (0, 0), mask=wm)
            transparent.show()
            rgb_transparent = wm.convert('RGB')
            rgb_transparent.save(outfile, "JPEG")

button = Button(text="Upload File", highlightthickness=0, command=open_img_file)
button.grid(row=1, column=0)


window.mainloop()
