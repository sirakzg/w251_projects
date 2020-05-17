sudo docker run --name mqtt_broker1 -v ~/w251_projects/week3hw/:/w251 --env MQTT_CONFIG='/w251/jtx2_broker.conf' -d mqtt_broker
sudo docker run --name mqtt_forwarder -v ~/w251_projects/week3hw/:/w251 --env MQTT_CONFIG='/w251/jtx2_forwarder.conf' -d mqtt_broker

