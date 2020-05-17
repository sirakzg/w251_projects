sudo docker run --name face-detector -e DISPLAY=$DISPLAY --privileged --network face-bridge --env QT_X11_NO_MITSHM=1 --rm -d face-detect
sudo docker run --name mqtt_broker1 --network face-bridge -v ~/w251_projects/week3hw/:/w251 --env MQTT_CONFIG='/w251/jtx2_broker.conf' --rm -d mqtt_broker
sudo docker run --name jtx2_forwarder --network face-bridge -v ~/w251_projects/week3hw/:/w251 --env MQTT_CONFIG='/w251/jtx2_forwarder.conf' --rm -d mqtt_broker

