import time
import picamera

def recordVideo(filename):
    with picamera.PiCamera() as camera:
        camera.resolution = (800, 600)
        camera.start_preview()
        camera.start_recording(filename + '.h264')
        camera.wait_recording(5)
        camera.capture(filename + '.jpg', use_video_port=True)
        camera.wait_recording(5)
        camera.stop_recording()

recordVideo("newfile")