from distutils.cmd import Command
from pickle import TRUE
from tkinter import Button, Tk, Label, X, Frame, Y, LEFT, BOTH
import cv2
from tkinter import *
from PIL import Image, ImageTk   
import sys
import re
root = Tk()
import queue
import threading
from collections import deque
from rovlib.cameras import RovCam

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

root.geometry("%dx%d" % (width, height))

root.title("ROV")

# Initialize frames
root.attributes('-fullscreen', True)
def touch_1(n,width,height,index):
    dim = (width,height)
    new_window = Toplevel(root)
    new_window.title("camera " + index)
    new_window.geometry("%dx%d" % (width, height))

    f3 = Frame(new_window, bg="pink")    
    f3.pack(fill=BOTH, expand=True)
    w4 = Label(f3, text="Blue", bg="blue", fg="white")
    w4.pack(side=LEFT, fill=BOTH, expand=True)
    while True:
        if len(camera_queue)!= 0: 
            frame ,source  = camera_queue.popleft()
            if source ==index:
                cv2image= cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                img = cv2.resize(cv2image, dim,fx = 2, fy = 2, interpolation = cv2.INTER_AREA)
                img = Image.fromarray(img)
                imgtk = ImageTk.PhotoImage(image = img)
                w4.imgtk = imgtk
                w4.configure(image=imgtk)
                root.update_idletasks()
                root.update()
            else:
                break
        
  
def close():
     root.destroy()  

camera_queue = deque()
def camera_reader(source, camera_queue,index):
    print("Cam Loading...")
    cap = RovCam(source)
    print("Cam Loaded...")
    while(True):
        ret,frame = cap.read()
        if frame is not None:
            camera_queue.append([frame,index]) 
        else:
            cap = RovCam(source)   
           

camera_read = threading.Thread(target=camera_reader, args=(RovCam.FRONT, camera_queue,"FRONT"))
camera_read.daemon = True
camera_read.start() 

camera_read = threading.Thread(target=camera_reader, args=(RovCam.ARM, camera_queue,"ARM"))
camera_read.daemon = True
camera_read.start() 

# camera_read = threading.Thread(target=camera_reader, args=(RovCam.MAX_DATAGRAM, camera_queue,2))
# camera_read.daemon = True
# camera_read.start() 


  

f1 = Frame(root, bg="grey")
f2 = Frame(root, bg="pink")

# Initialize labels
labels = (Label(f1, text="Red", bg="black", fg="white",height=3),
          Label(f1, text="Green", bg="green", fg="white")
          ,Label(f2, text="Red", bg="red", fg="white")
         , Label(f2, text="Blue", bg="blue", fg="white") )


b1 = Button(labels[0],text = "Button 1",width=15,command=lambda:touch_1(width,height,"FRONT"))
b2 = Button(labels[0],text = "Button 2",width=15,command=lambda:touch_1(width,height,"ARM"))
b3 = Button(labels[0],text = "Button 3",width=15,command=lambda:touch_1(width,height,2))
b4 = Button(labels[0],text = "quit",width=15,command=close)



# Packing level 1
f1.pack(fill=X)
f2.pack(fill=BOTH, expand=True)

# Packing level 2
labels[0].pack(fill=X)
labels[1].pack(fill=X)
b1.pack(side="left")
b2.pack(side="left")
b3.pack(side="left")
b4.pack(side="left")

labels[2].pack(side=LEFT, fill=BOTH, expand=True)

labels[3].pack(side=LEFT, fill=BOTH, expand=True)


dim1 = (width//2,height//2)


dim = [(width//2,height//2),(width//2,height//2),(width//2,height//2)]
    

while True:
    if len(camera_queue)!=0:
        frame ,source  = camera_queue.popleft()
        cv2image= cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        img1 = cv2.resize(cv2image,dim[source+1],fx=1,fy=1, interpolation = cv2.INTER_AREA)
    
        img1 = Image.fromarray(img1)
        
        #img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        imgtk = ImageTk.PhotoImage(image = img1)
        
        labels[source+1].imgtk = imgtk
        labels[source+1].configure(image=imgtk)
        

        root.update_idletasks()
        root.update()      