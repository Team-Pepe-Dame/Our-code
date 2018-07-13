# Step 1,
###  Installing Mosquitto MQTT client on Rapsberry Pi

*	sudo -i
*	wget http://repo.mosquitto.org/debian/mosquitto-repo.gpg.key
*	sudo apt-key add mosquitto-repo.gpg.key 
*	cd /etc/apt/sources.list.d/
*	wget http://repo.mosquitto.org/debian/mosquitto-stretch.list
*	apt-get update
*	apt-get install mosquitto-clients

# Step 2,
###  Look at MQTT/Mosquitto Information
###  Beginners Guide To The MQTT Protocol
###  http://www.steves-internet-guide.com/mqtt/
# Step 3,
###  Look at guide to using mosquitto_pub and mosquitto_sub
###  Using The Mosquitto_pub and Mosquitto_sub MQTT Client Tools- Examples
###  http://www.steves-internet-guide.com/mosquitto_pub-sub-clients/
# Step 4,
###  Using the internet server at 82.165.16.151 
###  Set up a classroom wide chat room

#### e.g. In One window
*        mosquitto_sub -h 82.165.16.151 -t UCC/mark

####      In another window
*        mosquitto_pub -h 82.165.16.151 -m "Hi" -t UCC/mark

# Step 5,
### Build a python script to monitor the health of your pi
### CPU, RAM and disk monitoring using python
### From: https://www.raspberrypi.org/forums/viewtopic.php?t=22180
# Step 6,
### Publish health information using MQTT
#### e.g.
* mosquitto_pub -h 82.165.16.151 -m "$(./monitor.py)" -t UCC/mark/api1.0/pihealth

#### and read it back
* mosquitto_sub -h 82.165.16.151 -t UCC/mark/api1.0/pihealth

# Step 7,
### Read back the health of everyones pi
# Step 8,
### Aggregate and display the data
# Step 9,
### See how to use Python directly to talk to MQTT
###  Using Paho in python with MQTT
###  http://www.steves-internet-guide.com/into-mqtt-python-client/
