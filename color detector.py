import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from colorthief import ColorThief

root = Tk()
root.title("Color detector")
root.geometry("800x470+100+100")
root.configure(bg="#e4e8eb")
root.resizable(False, False)

filename = None

# ---------------- SHOW IMAGE ---------------- #

def showimage():
    global filename
    filename = filedialog.askopenfilename(
        title="Select Image",
        filetypes=(("PNG files","*.png"),("JPG files","*.jpg"),("All files","*.*"))
    )

    img = Image.open(filename)
    img = img.resize((310,270))
    img = ImageTk.PhotoImage(img)

    lbl.configure(image=img)
    lbl.image = img


# ---------------- EXTRACT COLORS ---------------- #

def extractcolor():

    if not filename:
        return

    ct = ColorThief(filename)
    palette = ct.get_palette(color_count=10)

    hex_colors = []

    for rgb in palette:
        hex_color = '#%02x%02x%02x' % rgb
        hex_colors.append(hex_color)

    # Update canvas colors
    colors.itemconfig(id1, fill=hex_colors[0])
    colors.itemconfig(id2, fill=hex_colors[1])
    colors.itemconfig(id3, fill=hex_colors[2])
    colors.itemconfig(id4, fill=hex_colors[3])
    colors.itemconfig(id5, fill=hex_colors[4])

    colors2.itemconfig(id6, fill=hex_colors[5])
    colors2.itemconfig(id7, fill=hex_colors[6])
    colors2.itemconfig(id8, fill=hex_colors[7])
    colors2.itemconfig(id9, fill=hex_colors[8])
    colors2.itemconfig(id10, fill=hex_colors[9])

    # Update labels
    hex1.config(text=hex_colors[0])
    hex2.config(text=hex_colors[1])
    hex3.config(text=hex_colors[2])
    hex4.config(text=hex_colors[3])
    hex5.config(text=hex_colors[4])
    hex6.config(text=hex_colors[5])
    hex7.config(text=hex_colors[6])
    hex8.config(text=hex_colors[7])
    hex9.config(text=hex_colors[8])
    hex10.config(text=hex_colors[9])


# ---------------- ICON ---------------- #

image_icon = PhotoImage(file="icon.png")
root.iconphoto(False, image_icon)


# ---------------- MAIN FRAME ---------------- #

frame = Frame(root, width=700, height=370, bg="#fff")
frame.place(x=50, y=50)

logo = PhotoImage(file="logo.png")

Label(frame, image=logo, bg="#fff").place(x=10, y=10)
Label(frame, text="Color detector", font="arial 20 bold", bg="white").place(x=60, y=20)


# ---------------- COLORS COLUMN 1 ---------------- #

colors = Canvas(frame, bg="#fff", width=150, height=265, bd=0)
colors.place(x=20,y=90)

id1 = colors.create_rectangle(10,10,50,50, fill="#b8255f")
id2 = colors.create_rectangle(10,60,50,100, fill="#db4035")
id3 = colors.create_rectangle(10,110,50,150, fill="#ff9933")
id4 = colors.create_rectangle(10,160,50,200, fill="#fcb900")
id5 = colors.create_rectangle(10,210,50,250, fill="#cc49bb")

hex1 = Label(colors,text="#b8255f",font="arial 12 bold",bg="white")
hex1.place(x=60,y=15)

hex2 = Label(colors,text="#db4035",font="arial 12 bold",bg="white")
hex2.place(x=60,y=65)

hex3 = Label(colors,text="#ff9933",font="arial 12 bold",bg="white")
hex3.place(x=60,y=115)

hex4 = Label(colors,text="#fcb900",font="arial 12 bold",bg="white")
hex4.place(x=60,y=165)

hex5 = Label(colors,text="#cc49bb",font="arial 12 bold",bg="white")
hex5.place(x=60,y=215)


# ---------------- COLORS COLUMN 2 ---------------- #

colors2 = Canvas(frame, bg="#fff", width=150, height=265, bd=0)
colors2.place(x=180,y=90)

id6 = colors2.create_rectangle(10,10,50,50, fill="#7ecc49")
id7 = colors2.create_rectangle(10,60,50,100, fill="#fcb900")
id8 = colors2.create_rectangle(10,110,50,150, fill="#ff9933")
id9 = colors2.create_rectangle(10,160,50,200, fill="#db4035")
id10 = colors2.create_rectangle(10,210,50,250, fill="#7625b8")

hex6 = Label(colors2,text="#7ecc49",font="arial 12 bold",bg="white")
hex6.place(x=60,y=15)

hex7 = Label(colors2,text="#fcb900",font="arial 12 bold",bg="white")
hex7.place(x=60,y=65)

hex8 = Label(colors2,text="#ff9933",font="arial 12 bold",bg="white")
hex8.place(x=60,y=115)

hex9 = Label(colors2,text="#db4035",font="arial 12 bold",bg="white")
hex9.place(x=60,y=165)

hex10 = Label(colors2,text="#7625b8",font="arial 12 bold",bg="white")
hex10.place(x=60,y=215)


# ---------------- IMAGE PANEL ---------------- #

selectimage = Frame(frame,width=340,height=350,bg="#fff",bd=2,relief=GROOVE)
selectimage.place(x=350,y=10)

f = Frame(selectimage,bd=3,bg="black",width=320,height=280,relief=GROOVE)
f.place(x=10,y=10)

lbl = Label(f,bg="black")
lbl.pack()


Button(selectimage,text="Select Image",font="arial 12 bold",
       command=showimage).place(x=40,y=300)

Button(selectimage,text="Extract Colors",font="arial 12 bold",
       command=extractcolor).place(x=180,y=300)


root.mainloop()