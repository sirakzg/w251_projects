docker run --name cloud-broker -p 1883:1883 --network face-bridge -v ~/w251_projects/week3hw:/w251 --env MQTT_CONFIG='/w251/cloud_broker.conf' --rm -d mqtt_broker
docker run --name image-saver --network face-brid --env SAVE_FOLDER='/ibmcloud' --rm -d -v /mnt/ibm-objstore:/ibmcloud/w251 image-saver
