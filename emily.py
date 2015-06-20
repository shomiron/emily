import time
import picamera
from PIL import Image


def recordVideo(filename):
    with picamera.PiCamera() as camera:
        camera.resolution = (640, 480)
        camera.vflip = True
        camera.start_preview()
        camera.start_recording("../video-records/" + filename + '.h264')
        camera.wait_recording(5)
        camera.capture("../image-records/" + filename + '.jpg', use_video_port=True)
        camera.wait_recording(5)
        camera.stop_recording()

def checkTamper(filename):
    im = Image.open("../image-records/" + filename + '.jpg')
    pxarray = im.getdata()
    for px in pxarray:
        print px


filename = "evid-" + time.strftime("%d%m%Y-%H%M%S")
recordVideo(filename)
checkTamper(filename)