import queue, threading
from queue import Queue
import cv2


COUNT = 0

class system_manager():
    def __init__(self, source):
        global COUNT
        ## camera reader
        self.camera_queue = queue.Queue(maxsize=20)
        self.camera_reader = threading.Thread(target=camera_reader, args=(source, self.camera_queue))
        self.camera_reader.daemon = True
        self.camera_reader.start()
        self.camera_display = threading.Thread(target=camera_display, args=(self.camera_queue, "lol"+str(COUNT),))
        # self.camera_display.daemon = True
        self.camera_display.start()
        COUNT += 1


def camera_reader(source, camera_queue):
    print("Cam Loading...")
    cap = cv2.VideoCapture(source)
    print("Cam Loaded...")
    while(True):
        ret, frame = cap.read()
        if ret:
            camera_queue.put(frame)


def camera_display(camera_queue, window_name):
    print("doing something")
    while(True):
        frame = camera_queue.get()
        key = cv2.waitKey(1)
        if (key == ord('q')):
            break
        cv2.imshow(window_name, frame)



if __name__ == "__main__":
    SM = system_manager(source=0)
    SM = system_manager(source=1)
    SM = system_manager(source=2)





