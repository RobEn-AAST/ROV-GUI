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
import multiprocessing
import random
import os

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

root.geometry("%dx%d" % (width, height))

root.title("ROV")



# Initialize frames
root.attributes('-fullscreen', True)
def touch_1(width,height,index):
    dim = (width,height)
    new_window = Toplevel(root)
    new_window.title("camera " + str(index))
    new_window.geometry("%dx%d" % (width, height))

    f3 = Frame(new_window, bg="pink")    
    f3.pack(fill=BOTH, expand=True)
    w4 = Label(f3, text="Blue", bg="blue", fg="white")
    w4.pack(side=LEFT, fill=BOTH, expand=True)
    while True:
        new_window.update_idletasks()
        new_window.update()
        if len(camera_queue)!= 0: 
            frame ,source  = camera_queue.popleft()
            if source ==index:
                cv2image= cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                img = cv2.resize(cv2image, dim,fx = 2, fy = 2, interpolation = cv2.INTER_AREA)
                img = Image.fromarray(img)
                imgtk = ImageTk.PhotoImage(image = img)
                w4.imgtk = imgtk
                w4.configure(image=imgtk)

        
  
def close():
     root.destroy()  

camera_queue = deque()
def camera_reader(source, camera_queue,index):
    print("Cam Loading...")
    cap = RovCam(source)
    print("Cam Loaded...")
    while(True):
        frame = cap.read()
        if frame is not None:
            camera_queue.append([frame,index]) 
        else:
            cap = RovCam(source)
       
           

camera_read = threading.Thread(target=camera_reader, args=(RovCam.FRONT, camera_queue,1))
camera_read.daemon = True
camera_read.start() 

camera_read = threading.Thread(target=camera_reader, args=(RovCam.ARM, camera_queue,0))
camera_read.daemon = True
camera_read.start() 

# camera_read = threading.Thread(target=camera_reader, args=(RovCam.MAX_DATAGRAM, camera_queue,2))
# camera_read.daemon = True
# camera_read.start() 


  

f1 = Frame(root, bg="grey")
f2 = Frame(root, bg="pink")

img_arr=[]
for image in os.listdir('photos'):
    imag = os.path.join('photos',image)
    img_arr.append(imag)

photos=random.sample(img_arr,2)

photo1=photos[0]
photo2=photos[1]
img_right=Image.open(photo2)
img_left=Image.open(photo1)
img_right=img_right.resize((width//4,height//2))
img_left=img_left.resize((width//4,height//2))
img_right=ImageTk.PhotoImage(img_right)
img_left=ImageTk.PhotoImage(img_left)

photo_left=Label(f1,bg="white", image=img_left)
photo_right=Label(f1,bg="white", image=img_right)

# Initialize labels
labels = (Label(f1, text="Red", bg="black", fg="white",height=3),
          Button(f1, text="", bg="white", fg="black",relief="sunken",command=lambda:multiprocessing.Process(target=touch_1(width,height,0).start().join()))
          ,Button(f2, text="", bg="white", fg="black",relief="sunken",command=lambda:multiprocessing.Process(target=touch_1(width,height,1).start().join() ))
         , Button(f2, text="", bg="white", fg="black",relief="sunken",command=lambda:multiprocessing.Process(target=touch_1(width,height,2).start().join() )
         )) 


# b1 = Button(labels[0],text = "Button 1",width=15,command=lambda:touch_1(width,height,1))
# b2 = Button(labels[0],text = "Button 2",width=15,command=lambda:touch_1(width,height,0))
# b3 = Button(labels[0],text = "Button 3",width=15,command=lambda:touch_1(width,height,2))
# b4 = Button(labels[0],text = "quit",width=15,command=close)



# Packing level 1
buttom_exit = Button(labels[0],text = "X",bg="red",fg="white",font=3,relief="sunken",width=10,command=close)


# Packing level 1
f1.pack(fill=X)
f2.pack(fill=BOTH, expand=True)



# Packing level 2
labels[0].pack(fill=X)
photo_left.pack(side=LEFT, fill=BOTH, expand=True)
photo_right.pack(side=RIGHT, fill=BOTH, expand=True)




labels[1].pack(fill=X)



# b1.pack(side="left")
# b2.pack(side="left")
# b3.pack(side="left")
# b4.pack(side="left")

buttom_exit.pack(side="right")

labels[2].pack(side=LEFT, fill=BOTH, expand=True)

labels[3].pack(side=LEFT, fill=BOTH, expand=True)


dim1 = (width//2,height//2)


dim = [(width//2,height//2),(width//2,height//2),(width//2,height//2)]
    

while True:
    if len(camera_queue)!=0 :
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