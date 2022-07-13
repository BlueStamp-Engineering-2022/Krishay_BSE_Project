import cv2
import sys
from mail import sendEmail
from flask import Flask, render_template, Response
from camera import VideoCamera
from flask_basicauth import BasicAuth
import time
import threading

# Sends an email only once in this time interval
email_update_interval = 30

# Creates a camera object, flip vertically
video_camera = VideoCamera(flip=True)

# Adds the OpenCV classifier for recognizing objects
object_classifier = cv2.CascadeClassifier("models/facial_recognition_model.xml")

# App Global
app = Flask(__name__, template_folder='templates')

# Authentication for security feed
app.config['BASIC_AUTH_USERNAME'] = 'krishay'
app.config['BASIC_AUTH_PASSWORD'] = 'bluestamp'
app.config['BASIC_AUTH_FORCE'] = True

basic_auth = BasicAuth(app)
last_epoch = 0

# Continuously checks for objects
def check_for_objects():
	global last_epoch
	while True:
		try:
			frame, found_obj = video_camera.get_object(object_classifier)
			if found_obj and (time.time() - last_epoch) > email_update_interval:
				last_epoch = time.time()
				print "Sending email..."
				sendEmail(frame)
				print "done!"
		except:
			print "Error sending email: ", sys.exc_info()[0]

# Initializes website
@app.route('/')
@basic_auth.required
def index():
    return render_template('index.html')

@app.route('/design')
def design():
    return render_template('design.html')

@app.route('/camerapy')
def camerapy():
    return render_template('camerapy.html')

@app.route('/mailpy')
def mailpy():
    return render_template('mailpy.html')

@app.route('/mainpy')
def mainpy():
    return render_template('mainpy.html')

# Gets each frame from the camera and adds that to the website
def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

# Initializes video feed
@app.route('/video_feed')
def video_feed():
    return Response(gen(video_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')



# Runs camera
if __name__ == '__main__':
    t = threading.Thread(target=check_for_objects, args=())
    t.daemon = True
    t.start()
    app.run(host='0.0.0.0', debug=False)
