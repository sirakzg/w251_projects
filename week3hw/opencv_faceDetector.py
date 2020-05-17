import numpy as np
import cv2
import time

import paho.mqtt.client as mqtt

# load the OpenCV face classifier
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# 1 should correspond to /dev/video1 , your USB camera. The 0 is reserved for the TX2 onboard camera
cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)
cap.set(cv2.CAP_PROP_FPS, 12)



LOCAL_MQTT_HOST="mqtt_broker1"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="face_detect"

def on_connect_local(client, userdata, flags, rc):
        print("connected to local broker with rc: " + str(rc))
        client.subscribe(LOCAL_MQTT_TOPIC)
	

client = mqtt.Client()
client.on_connect = on_connect_local
client.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)


while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()

	# We don't use the color information, so might as well save space
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	# face detection and other logic goes here
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	for (x,y,w,h) in faces:
		# your logic goes here; for instance
		# cut out face from the frame..
		# rc,png = cv2.imencode('.png', face)
		# msg = png.tobytes()
		# ...
		#print("Face: ",x,y,w,h)

		# publish face!
		crop = cv2.imencode(".png", gray[y:y+h,x:x+w])[1].tobytes()
		client.publish("face_detect", crop, qos=1)

		# draw on gray image for imshow
		gray = cv2.rectangle(gray, (x,y), (x+w,y+h), (0,0,0), 2)


	# Display the resulting frame
	#cv2.imshow('frame',gray)
	#if cv2.waitKey(1) & 0xFF == ord('q'):
	#   break

	time.sleep(1)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

