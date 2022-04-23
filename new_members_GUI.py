from distutils.cmd import Command
from pickle import TRUE
from tkinter import Button, Tk, Label, X, Frame, Y, LEFT, BOTH
import cv2
from tkinter import *
from PIL import Image, ImageTk
import threading

   
import sys
import re
root = Tk()

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))
root.title("ROV")

root.attributes('-fullscreen', True)

def touch_1(n,width,height):
    

    camera_cap = cv2.VideoCapture(0)
    camera_cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2160)
    camera_cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    dim = (width,height)
    new_window= Toplevel(root)
    new_window.title("camera " + str(n))
    new_window.geometry("%dx%d" % (width, height))

    f3 = Frame(new_window, bg="pink")    
    f3.pack(fill=BOTH, expand=True)
    w4 = Label(f3, text="Blue", bg="blue", fg="white")
    w4.pack(side=LEFT, fill=BOTH, expand=True)
    
    
    while True:
            
        
        ret,cameras_frame = camera_cap.read()
        cv2image= cv2.cvtColor(cameras_frame,cv2.COLOR_BGR2RGB)
        img = Image.fromarray(cv2image)
       
        imgtk = ImageTk.PhotoImage(image = img)
        w4.imgtk = imgtk
        w4.configure(image=imgtk)
        w4.update_idletasks()
        w4.update()

    

         
  
def close():
     root.destroy()  

     

f1 = Frame(root, bg="grey")
f2 = Frame(root, bg="pink")

# Initialize labels
w1 = Label(f1, text="Red", bg="black", fg="white",height=3)
w2 = Label(f1, text="Green", bg="green", fg="white")

b1 = Button(w1,text = "Button 1",width=15,command=lambda:touch_1(1,width,height))

b2 = Button(w1,text = "Button 2",width=15,command=lambda:touch_1(1,width,height))
b3 = Button(w1,text = "Button 3",width=15,command=lambda:touch_1(1,width,height))
b4 = Button(w1,text = "quit",width=15,command=close)

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
    print (ret)
    if ret!= True:
        camera_caps =cv2.VideoCapture(0)
        camera_caps.set(4,400)
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
