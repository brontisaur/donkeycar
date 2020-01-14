import cv2
import time

class cvWebcam(object):
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.frame = None

    def run(self):
        _, self.frame = self.cap.read()
        return self.frame
    
    def shutdown(self):
        self.cap.release()

class cvShow(object):
    
    def run(self, image):
        cv2.imshow('frame', image)
        cv2.waitKey(1)

    def shutdown(self):
        cv2.destroyAllWindows()
