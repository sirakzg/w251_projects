# Homework 3 - Internet of Things 101

The goal of this assignment is to stream captured face data from a webcam connected to a Jeston TX2, and store it in cloud storage using IBM's S3 buckets. The following is a diagram highlighting the connections between all the containers.

<img src="HWeek3-diagram.png" width="75%" height="75%" />

## Jetson Containers

### Face Detector

### MQTT Broker

### MQTT Forwarder

## Cloud containers

### Cloud Broker

### Image Saver

## MQTT Settings

The MQTT protocal provides a couple communication options in the name of the topic, and the desired quality of service (QoS) to use for each message.  For this submission I used the topic `face_detect/#`, with the wildcard ending to support additional levels.  I used `QoS=1`, which guarantees packets are sent at least once until a confirmation packet is receieved.

## Sample Images
https://objects-sirakzg-w251.s3.us-east.cloud-object-storage.appdomain.cloud/w251/face_1589745673.png

<img src="https://objects-sirakzg-w251.s3.us-east.cloud-object-storage.appdomain.cloud/w251/face_1589745673.png" />

https://objects-sirakzg-w251.s3.us-east.cloud-object-storage.appdomain.cloud/w251/face_1589745705.png

<img src="https://objects-sirakzg-w251.s3.us-east.cloud-object-storage.appdomain.cloud/w251/face_1589745705.png" />


For instructions on this assignment see https://github.com/MIDS-scaling-up/v2/tree/master/week03/hw.
