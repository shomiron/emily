import time
import picamera


def recordVideo(filename):
    with picamera.PiCamera() as camera:
        camera.resolution = (640, 480)
        camera.vflip = True
        camera.start_preview()
        camera.start_recording(filename + '.h264')
        camera.wait_recording(5)
        camera.capture(filename + '.jpg', use_video_port=True)
        camera.wait_recording(5)
        camera.stop_recording()


filename = "evid-" + time.strftime("%d%m%Y-%H%M%S")
recordVideo(filename)