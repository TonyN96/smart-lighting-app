#!/usr/bin/python3

# Script used as MQTT subscriber to change state of LED

import light
import paho.mqtt.client as mqtt
from urllib.parse import urlparse
from gpiozero import LED
import sys

# Define event callbacks
def on_connect(client, userdata, flags, rc):
    print("Connection Result: " + str(rc))

def on_message(client, obj, msg):
    # If statements which change state of LED depending on message payload
    if msg.payload == b"ON":
        light.light_on()
    if msg.payload == b"OFF":
        light.light_off()

def on_subscribe(client, obj, mid, granted_qos):
    print("Subscribed, QOS granted: "+ str(granted_qos))

mqttc = mqtt.Client()

# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

# parse mqtt url for connection details
url_str = sys.argv[1]
url = urlparse(url_str)
base_topic = url.path[1:]

# Connect
if (url.username):
    mqttc.username_pw_set(url.username, url.password)
print(url.hostname)
print(url.port)
mqttc.connect(url.hostname, url.port)

# Start subscribe, with QoS level 0
mqttc.subscribe(base_topic, 0)
mqttc.loop_forever()