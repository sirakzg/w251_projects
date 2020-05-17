import sys
import os
import time
import cv2
import numpy as np

import paho.mqtt.client as mqtt

if len(sys.argv) != 2 or not os.path.isdir(sys.argv[1]):
	print("Help: run command as $>image_saver.py <output folder>")
	exit()


LOCAL_MQTT_HOST="cloud-broker"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="face_detect"

def on_connect_local(client, userdata, flags, rc):
	print("connected to local broker with rc: " + str(rc))
	client.subscribe(LOCAL_MQTT_TOPIC)
	
def on_message(client,userdata, msg):
	try:
		print("message received!", int(time.time()) )	
		# if we wanted to re-publish this message, something like this should work
		# msg = msg.payload
		# remote_mqttclient.publish(REMOTE_MQTT_TOPIC, payload=msg, qos=0, retain=False)

		nparr = np.fromstring(msg.payload, np.uint8)
		img = cv2.imdecode(nparr,  cv2.IMREAD_GRAYSCALE)

		# opencv to save to file
		cv2.imwrite( os.path.join(sys.argv[1], "face_"+str(int(time.time()))+".png"), img)

	except:
		print("Unexpected error:", sys.exc_info()[0])

local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
local_mqttclient.on_message = on_message



# go into a loop
local_mqttclient.loop_forever()
