# This Broker is catching messages from 4 devices so it will need to retain messages.
import helper
import network
import time
from umqtt.simple import MQTTClient

# WiFi connect
SSID = 'YOUR_SSID'
password = 'YOUR_PASSWORD'

# IoT Hub
iot_hub_broker = 'IOT_HUB_BROKER_URL'  # It will be Private Broker because the micropython umqtt won't work for public brokers 
iot_hub_port = 1883 
iot_hub_topic = 'Catch_data' 

# Setting up WiFi connection
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

while not wlan.isconnected():
    time.sleep(1)

print("Connected to WiFi")
print("IP Address:", wlan.ifconfig()[0])

# Callback function to handle received messages
def sub_cb(topic, msg):
    print("Received message:", msg)  # All messages are redirected Automatically 
    # Forward the message to the IoT hub
    iot_client.publish(iot_hub_topic, msg)

# Set up the MQTT client for receiving messages
receiver_broker = 'YOUR_RECEIVER_BROKER_IP'  # This is the Broker that the other picos will use or i could use websockets.
receiver_topic = 'from_pico'

receiver_client = MQTTClient("pico_receiver", receiver_broker)
receiver_client.set_callback(sub_cb)
receiver_client.connect()
receiver_client.subscribe(receiver_topic)

# Set up the MQTT client for the IoT hub
iot_client = MQTTClient("pico_to_iot", iot_hub_broker, port=iot_hub_port)
iot_client.connect()

while True:
    try:
        receiver_client.check_msg()   # Loop this section forever
    except KeyboardInterrupt:
        print("Disconnecting...")      # Don't rely on one loop, repeat for multiple loops. 
        receiver_client.disconnect()
        iot_client.disconnect()
        break
