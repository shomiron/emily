import time
import picamera
from PIL import Image


def recordVideo(filename):
    with picamera.PiCamera() as camera:
        camera.resolution = (320, 240)
        # PiCamera setting 
        # - https://www.raspberrypi.org/documentation/usage/camera/python/README.md
        # - http://picamera.readthedocs.org/en/latest/api_camera.html
        camera.vflip = True
        camera.exposure_mode = 'night'
        camera.meter_mode = 'average'
        camera.awb_mode = 'auto'
        camera.capture("../image-records/" + filename + '.jpg', use_video_port=True)
        # camera.start_preview()
        camera.resolution = (800, 600)
        camera.start_recording("../video-records/" + filename + '.h264')
        camera.wait_recording(1)

        camera.wait_recording(5)
        camera.stop_recording()

def checkTamper(filename):
    im = Image.open("../image-records/" + filename + '.jpg')
    pxarray = im.getdata()
    cntr = 0
    for px in pxarray:
        minv = min(px)
        maxv = max(px)
        if maxv - minv < 10:
            cntr += 1
    totalpx = len(pxarray)
    prcnt = 0.0000
    prcnt = (float(cntr) / float(totalpx)) * 100
    if int(prcnt) > 75:
        return 1
    else:
        return 0


filename = "evid-" + time.strftime("%d%m%Y-%H%M%S")
recordVideo(filename)
if checkTamper(filename) == 1:
    print "BLOW SIREN"
