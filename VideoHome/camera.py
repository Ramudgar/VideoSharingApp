from django.core.mail import EmailMessage
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import cv2
import threading
import numpy as np
class VideoCamera(object):
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        (self.grabbed, self.frame)= self.cap.read()
        threading.Thread(target=self.update, args=()).start()
    def __del__(self):
        self.cap.remove()
    def get_frame(self):
        ret, frame = self.cap.read()
        frame_flip = cv2.flip(frame, 1)
        ret, frame = cv2.imencode('.jpg', frame_flip)
        return frame.tobytes()

    def update(self):
        while True:
         (self.grabbed, self.frame) = self.cap.read()


    def gen(camera):
        while True:
            frame = camera.get_frame()
            yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')