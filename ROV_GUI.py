from time import time, sleep
from tkinter import *
from PIL import Image, ImageTk
import cv2
import threading

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

# label2 =Label(win,width = 400, height = 400)
# # label2.grid(row = 1, column=0)
# label2.place(x = 600 , y= 0)

# label3 =Label(win,width = 400, height = 400)
# # label3.grid(row = 2, column=0)





camera_caps = cv2.VideoCapture(0), cv2.VideoCapture(1), cv2.VideoCapture(2)


def get_frames():
    global camera_caps
    return camera_caps[0].read(), camera_caps[1].read(), camera_caps[2].read()



def show_frames():
    global labels, cap1, cap2, cap3, win
    while True:
        cameras_frame = get_frames()
        for i in range(len(cameras_frame)):
            if cameras_frame[i][0]:
                # Get the latest frame and convert into Image
                cv2image= cv2.cvtColor(cameras_frame[i][1],cv2.COLOR_BGR2RGB)
                img = Image.fromarray(cv2image)
                # Convert image to PhotoImage
                imgtk = ImageTk.PhotoImage(image = img)
                labels[i].imgtk = imgtk
                labels[i].configure(image=imgtk)
                # Repeat after an interval to capture continiously
                win.update_idletasks()
                win.update()
            else:
                try:
                    camera_caps[i].release()
                    cv2.destroyAllWindows()
                    
                except:
                    print("An exception occurred")
           

                   

show_frames()

# show_frames1()
# show_frames2()
# show_frames3()

# t1 = threading.Thread(target=show_frames(), args=(10,))
# t2 = threading.Thread(target=show_frames2(), args=(10,))
# t3 = threading.Thread(target=show_frames3(), args=(10,))

# t1.start()
#     # starting thread 2
# t2.start()
# t3.start()
  
#     # wait until thread 1 is completely executed
# t1.join()
#     # wait until thread 2 is completely executed
# t2.join()
# t3.join()
