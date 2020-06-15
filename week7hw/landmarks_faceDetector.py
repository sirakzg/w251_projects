import numpy as np
import cv2
import time

import paho.mqtt.client as mqtt

import tensorflow as tf
from tensorflow.keras import backend
from tensorflow.keras.models import Sequential, Model

from tensorflow.keras import optimizers
from tensorflow.keras.initializers import glorot_uniform, he_normal

from tensorflow.keras.layers import LeakyReLU
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Activation, Convolution2D, MaxPooling2D, BatchNormalization, Flatten, Dense, Dropout, Conv2D,MaxPool2D, ZeroPadding2D

# load the Facial Landmarks detector
from tensorflow.keras import backend as K
from tensorflow.keras.models import load_model

def root_mean_squared_error(y_true, y_pred):
        return K.sqrt(K.mean(K.square(y_pred - y_true)))

model = load_model('facial_landmarks.h5', custom_objects={'root_mean_squared_error': root_mean_squared_error})


# 1 should correspond to /dev/video1 , your USB camera. The 0 is reserved for the TX2 onboard camera
cap = cv2.VideoCapture(0)
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
	gray = cv2.resize(gray, (480,288))

	for i in range(0,5) :
		for j in range(0,3) :
			x = i*96
			y = j*96
			#
			#
			pred_imgs = np.expand_dims( gray[y:y+96,x:x+96], axis=2)
			pred_imgs = np.expand_dims(pred_imgs, axis=0)
			#print(pred_imgs.shape)
			a = model.predict(pred_imgs)[0]

			# Detected a face? show bounding box and send message
			if a[0] > 0 :

				minX = x + int(np.min(a[0::2]*96))
				minY = y + int(np.min(a[1::2]*96))
				maxX = x + int(np.max(a[0::2]*96))
				maxY = y + int(np.max(a[1::2]*96))

				gray = cv2.rectangle(gray, (minX,minY), (maxX,maxY), (0,0,0), 2)
				client.publish("face_detect", gray, qos=1)



	# Display the resulting frame
	cv2.imshow('frame',gray)
	if cv2.waitKey(1) & 0xFF == ord('q'):
	  break


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

