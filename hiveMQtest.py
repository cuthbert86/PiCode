import time
import paho.mqtt.client as paho
from paho import mqtt
import json
import time
from sense_hat import SenseHat
from datetime import datetime
from collections import deque

sense = SenseHat()
json_string = '{"temp": "36.24469757080078", "Humidity": "37.37043380737305", "Date": "2024-03-22 00:13:27.122036"}'
data1 = json.loads(json_string)
# Initialize deque with 120 None values
data_window = deque([], maxlen=120)
data_week = deque([], maxlen=840)
data_month = deque([], maxlen=3360)
temperature = float()
humidity = float()
date = data1["Date"]
day = float()
week = float()
month = float()
temp1 = float()
# Create an MQTT client instance
start_time = time.time()
duration = 1000
topic = "data1"


def calculate_rolling_averagemean(data):
    total = sum(data)
    num1 = len(data)
    aveMean = total / num1
#   ave1 = mean([data_window])
#   print(ave)
    return aveMean


# setting callbacks for different events to see if it works, print the message etc.
def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)


# with this callback you can see if your publish was successful
def on_publish(client, userdata, mid, properties=None):
    print("mid: " + str(mid))


# print which topic was subscribed to
def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


# print message, useful for checking if it was successful
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


# using MQTT version 5 here, for 3.1.1: MQTTv311, 3.1: MQTTv31
# userdata is user defined data of any type, updated by user_data_set()
# client_id is the given name of the client
client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect

# enable TLS for secure connection
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
# set username and password
client.username_pw_set("sub_1", "Subscribe123!")
# connect to HiveMQ Cloud on port 8883 (default for MQTT)
client.connect("d17bfaf8971f413c9d6d0df25dafb267.s1.eu.hivemq.cloud:8883", 8883)

# setting callbacks, use separate functions like above for better visibility
client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_publish = on_publish

# subscribe to all topics of encyclopedia by using the wildcard "#"
client.subscribe("test_data", qos=1)

# a single publish, this can also be done in loops, etc.
client.publish("encyclopedia/temperature", payload="hot", qos=1)

# loop_forever for simplicity, here you need to stop the loop manually
# you can also use loop_start and loop_stop
# client.loop_forever()

while (time.time() - start_time) < duration:
    data_window.appendleft(sense.get_temperature())
    data_week.appendleft(sense.get_temperature())
    data_month.appendleft(sense.get_temperature())
    data1 = {"temp": str(sense.get_temperature()),
             "Humidity": str(sense.get_humidity()),
             "Date": str(datetime.now()),
             "Ave1": str(calculate_rolling_averagemean(data_window)),
             "AveWeek": str(calculate_rolling_averagemean(data_week)),
             "AveMonth": str(calculate_rolling_averagemean(data_month)),
             }
    
    # Collect sensor data
    temperature = sense.get_temperature()
    humidity = sense.get_humidity()
    pressure = sense.get_pressure()
    timestamp = datetime.now().isoformat()
    print("Saved sensor data:", temperature, humidity, pressure, timestamp)

# Convert dictionary to JSON string
    message = json.dumps(data1)
    ave2 = calculate_rolling_averagemean(data_week)
# print(ave2)
    ave3 = calculate_rolling_averagemean(data_month)
# print (ave3)
    client.publish(topic, message)
    print(f"Published: {message} to topic: {topic}")
# Sleep for a short duration if needed
    time.sleep(10)
    client.publish("data1", payload=message, qos=1)
    rolling_avg = calculate_rolling_averagemean(data_window)
    print(f"Calculted Rolling averages: {data1}")
# Disconnect from the MQTT broker
else:
    client.disconnect()
