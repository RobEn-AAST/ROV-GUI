from queue import Queue
import queue
from time import time, sleep
from tkinter import *
from PIL import Image, ImageTk
import cv2
import threading
from queue import Queue

# Create an instance of TKinter Window or frame
win = Tk()

UN_AV_IMG = cv2.imread("unav.jpg", cv2.IMREAD_COLOR)



# Set the size of the window
win.geometry("1200x1200")

# Create a Label to capture the Video frames
labels = (Label(win, width = 400, height = 400),
        Label(win, width = 400, height = 400),
        Label(win, width = 400, height = 400))



labels[0].place(x = 0 , y= 0)
labels[1].place(x = 500 , y= 0)
labels[2].place(x = 500 , y= 500)



# global threads

def show_frames():
    camera_caps =[cv2.VideoCapture(0), cv2.VideoCapture(1), cv2.VideoCapture(2)]
    flag = 0
    while True:
        cameras_frame = camera_caps[0].read(), camera_caps[1].read(), camera_caps[2].read()
        
            # frames(i,cameras_frame)
        if cameras_frame[flag][0]:
            # Get the latest frame and convert into Image
            cv2image= cv2.cvtColor(cameras_frame[flag][1],cv2.COLOR_BGR2RGB)
            img = Image.fromarray(cv2image)
            # Convert image to PhotoImage
            imgtk = ImageTk.PhotoImage(image = img)
            labels[flag].imgtk = imgtk
            labels[flag].configure(image=imgtk)
                # Repeat after an interval to capture continiously
            win.update_idletasks()
            win.update()
            flag_handler(flag)
        else:
            camera_caps[flag] = cv2.VideoCapture(flag)
            print("An exception occurred") 
            flag_handler(flag)
 
def flag_handler(flag) :
    flag = flag+1
    if flag>=2:
        flag = 0            
        
            
            
                  

show_frames()


