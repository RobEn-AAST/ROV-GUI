from asyncio.windows_events import NULL
from distutils.cmd import Command
from doctest import master
from rovlib.cameras import RovCam

import queue
from tkinter import Button, Tk, Label, X, Frame, Y, LEFT, BOTH
import cv2
from tkinter import *
from PIL import Image, ImageTk   
import threading
from collections import deque
import random
import os

root = Tk(master)
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

big_Screen = deque()

root.geometry("%dx%d" % (width, height))

root.title("ROV")
# Initialize frames
root.attributes('-fullscreen', True)


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

camera_read = threading.Thread(target=camera_reader, args=(RovCam.MISC1, camera_queue,2))
camera_read.daemon = True
camera_read.start() 

def close():
    root.destroy() 

def rebuild(new_frame):
    new_frame.destroy()
    build_view()    


def touch_1(width,height,index,f1,f2):

    f1.pack_forget()
    f2.pack_forget()
    
    dim = (width,height)
    
   
    

    New_frame = Frame(root, bg="pink")  
    frame1 =Frame(root)
      

    label =Label(frame1, text="Red", bg="black", fg="white",height=3)
    buttom_exit = Button(label,text = "Back",bg="red",fg="white",font=3,relief="sunken",width=10,command=lambda: build_view(1,New_frame,frame1))

    frame1.pack(fill=X)
    New_frame.pack(fill=BOTH, expand=True)

    
    
    w4 = Label(New_frame, text="", bg="white", fg="black",relief="sunken")
    label.pack(fill=X)
    buttom_exit.pack(side="right")
    w4.pack(side=LEFT, fill=BOTH, expand=True)
    while True:
                
        if len(camera_queue)!= 0: 
            frame ,source  = camera_queue.popleft()
            if source == index:
                
                cv2image= cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                Screen_thread =threading.Thread(target=Resize, args=(cv2image,dim))
                Screen_thread.daemon = True
                Screen_thread.start() 
                Screen_thread.join()
                img1 = big_Screen.pop()
                img1 = Image.fromarray(img1)
                imgtk = ImageTk.PhotoImage(image = img1)
                w4.imgtk = imgtk
                w4.configure(image=imgtk)
                 

        root.update_idletasks()
        root.update()    
    
def Resize(img,dim):
   cv2image =cv2.resize(img, dim,fx = 2, fy = 2, interpolation = cv2.INTER_AREA)
   big_Screen.append(cv2image)
   


def build_view(i,frame1,frame2):

    if i == 1:
        frame1.pack_forget()
        frame2.pack_forget()

    

    f1 = Frame(root)
    f2 = Frame(root)

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

    labels = (Label(f1, text="Red", bg="black", fg="white",height=3),
                Button(f1, text="", bg="white", fg="black",relief="sunken",command=lambda:touch_1(width,height,0,f1,f2))
                ,Button(f2, text="", bg="white", fg="black",relief="sunken",command=lambda:touch_1(width,height,1,f1,f2))
                , Button(f2, text="", bg="white", fg="black",relief="sunken",command=lambda:touch_1(width,height,2,f1,f2) )
                )

    buttom_exit = Button(labels[0],text = "X",bg="red",fg="white",font=3,relief="sunken",width=10,command=close)

    f1.pack(fill=X)
    f2.pack(fill=BOTH, expand=True) 

    labels[0].pack(fill=X)
    photo_left.pack(side=LEFT, fill=BOTH, expand=True)
    photo_right.pack(side=RIGHT, fill=BOTH, expand=True)           

    labels[1].pack(fill=X)

    buttom_exit.pack(side="right")

    labels[2].pack(side=LEFT, fill=BOTH, expand=True)

    labels[3].pack(side=LEFT, fill=BOTH, expand=True)


    dim1 = (width//2,height//2)


    dim = [(width//2,height//2),(width//2,height//2),(width//2,height//2)]

    while True:
            if len(camera_queue)!=0 :
                frame ,source  = camera_queue.popleft()
                
                cv2image= cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                img1 = cv2.resize(cv2image,dim1,fx=1,fy=1, interpolation = cv2.INTER_AREA)
                
                img1 = Image.fromarray(img1)
                    
                    #img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
                imgtk = ImageTk.PhotoImage(image = img1)
                    
                labels[source+1].imgtk = imgtk
                labels[source+1].configure(image=imgtk)
                    

                root.update_idletasks()
                root.update()
    
build_view(0,NULL,NULL)      