from pickle import TRUE
from tkinter import Button, Tk, Label, X, Frame, Y, LEFT, BOTH
import cv2
from PIL import Image, ImageTk
root = Tk()

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))
root.title("ROV")
# Initialize frames



f1 = Frame(root, bg="grey")
f2 = Frame(root, bg="pink")

# Initialize labels
w1 = Label(f1, text="Red", bg="black", fg="white",height=3)
w2 = Label(f1, text="Green", bg="green", fg="white")

b1 = Button(w1,text = "Button 1",width=15)
b2 = Button(w1,text = "Button 2",width=15)
b3 = Button(w1,text = "Button 3",width=15)
b4 = Button(w1,text = "Button 4",width=15)

w1b = Label(f2, text="Red", bg="red", fg="white")
w3b = Label(f2, text="Blue", bg="blue", fg="white")



# Packing level 1
f1.pack(fill=X)
f2.pack(fill=BOTH, expand=True)

# Packing level 2
w1.pack(fill=X)
w2.pack(fill=X)
b1.pack(side="left")
b2.pack(side="left")
b3.pack(side="left")
b4.pack(side="left")

w1b.pack(side=LEFT, fill=BOTH, expand=True)

w3b.pack(side=LEFT, fill=BOTH, expand=True)

camera_caps =cv2.VideoCapture(0)
camera_caps.set(4,400)
while True:
    ret,cameras_frame = camera_caps.read()
    cv2image= cv2.cvtColor(cameras_frame,cv2.COLOR_BGR2RGB)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image = img)
    w3b.imgtk = imgtk
    w3b.configure(image=imgtk)
    w1b.imgtk = imgtk
    w1b.configure(image=imgtk)
    w2.imgtk = imgtk
    w2.configure(image=imgtk)

    root.update_idletasks()
    root.update()

root.mainloop()
