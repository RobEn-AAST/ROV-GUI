from queue import Queue
import queue
from time import time, sleep
# from tkinter import *
# from PIL import Image, ImageTk
import cv2
import threading
from queue import Queue

# win = Tk()

# UN_AV_IMG = cv2.imread("unav.jpg", cv2.IMREAD_COLOR)



# # Set the size of the window
# win.geometry("1200x1200")

# # Create a Label to capture the Video frames
# labels = (Label(win, width = 400, height = 400),
#         Label(win, width = 400, height = 400),
#         Label(win, width = 400, height = 400))



# labels[0].place(x = 0 , y= 0)
# labels[1].place(x = 500 , y= 0)
# labels[2].place(x = 500 , y= 500)


COUNT = 0
global frames

class system_manager():
    def __init__(self, source):
        global COUNT
        ## camera reader
        self.camera_queue = queue.Queue(maxsize=20)
        self.camera_reader = threading.Thread(target=camera_reader, args=(source, self.camera_queue))
        self.camera_reader.daemon = True
        self.camera_reader.start()
        self.camera_display = threading.Thread(target=camera_display, args=(self.camera_queue, "lol"+str(COUNT)))
        # self.camera_display.daemon = True
        self.camera_display.start()       
        COUNT += 1


def camera_reader(source, camera_queue):
    print("Cam Loading...")
    cap = cv2.VideoCapture(source)
    print("Cam Loaded...")
    while(True):
        ret,frame = cap.read()
        
        camera_queue.put(frame) 


def camera_display(camera_queue, window_name):
    print("doing something")
    
    while(True):
        frame = camera_queue.get()
        # frame = cv2.flip(frame, 1)
        # cv2image= cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        # imgtk = ImageTk.PhotoImage(image=Image.fromarray(cv2image))
        # labels[COUNT].imgtk = imgtk
        # labels[COUNT].configure(image=imgtk)
        
       
        key = cv2.waitKey(1)
        if (key == ord('q')):
            break
        cv2.imshow(window_name, frame)
       


if __name__ == "__main__":
    SM0 = system_manager(source=0)
    SM1 = system_manager(source=1)

    
    
    
        