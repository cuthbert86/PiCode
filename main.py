from helper import GetTemperature, connect_to_wifi, WifiServer, to_json
import network
import usocket
from time import time, sleep
import network
import time
from umqtt.simple import MQTTClient
import machine
from picozero import pico_temp_sensor
from machine import Pin
import micropython
import ustruct as struct
import json
import time
import random

adcpin = 4
sensor = machine.ADC(adcpin)
sock = usocket
SSID = 'BB'
WIFI_PASSWORD = b'***'
# SERVER_HOSTNAME = "e5d2174059b64286bd5f243dd055355a.s1.eu.hivemq.cloud:8884/mqtt"
Self_Name = 'PW_1'
USER = "Cuthbert"
# PASSWORD = 'Cbaines123!'
wlan = network.WLAN(network.STA_IF)
broker_address = "192.168.1.11"
adcpin = 4
sensor = machine.ADC(adcpin)
sock = usocket
SSID = 'BB'
PASSWORD = '6KH1jk1mn0s'
# SERVER_HOSTNAME = "e5d2174059b64286bd5f243dd055355a.s1.eu.hivemq.cloud:8884/mqtt"
USER = "Cuthbert"
TOPIC = "test_data"
wlan = network.WLAN(network.STA_IF)
mqtt = MQTTClient
#sending = broker_address 
BROKER = "192.168.1.11"
PORT = "1883"
CLIENT_ID = "Cuthbert"



Temperature = GetTemperature()
json_string = '{"Self Name": "PW_1", "temp":"27"}'
data1 = json.loads(json_string)



# Publish data

connect_to_wifi()
client = MQTTClient(CLIENT_ID, BROKER)

try:
    print("Connecting to MQTT broker...")
    client.connect()
    print("Connected to MQTT broker.")

    while True:
        Temperature = GetTemperature()
        json_result = to_json(Self_Name, Temperature)
        print (json_result)
        client.publish(TOPIC, json_result)
        time.sleep(5)  # Publish every 5 seconds
        Temperature = GetTemperature()
        json_result = to_json(Self_Name, Temperature)
        print(json_result)
        client.publish(TOPIC, json_result)
        time.sleep(5)
        Temperature = GetTemperature()
        json_result = to_json(Self_Name, Temperature)
        print (json_result)
        client.publish(TOPIC, json_result)
        Temperature = GetTemperature()
        json_result = to_json(Self_Name, Temperature)
        print (json_result)
        client.publish(TOPIC, json_result)
        
except Exception as e:
    print("An error occurred:", e)

try:
    print("Connecting to MQTT broker...")
    client.connect()
    print("Connected to MQTT broker.")

    while True:
        Temperature = GetTemperature()
        json_result = to_json(Self_Name, Temperature)
        print (json_result)
        client.publish(TOPIC, json_result)
        time.sleep(5)  # Publish every 5 seconds
        Temperature = GetTemperature()
        json_result = to_json(Self_Name, Temperature)
        print(json_result)
        client.publish(TOPIC, json_result)
        time.sleep(5)
        Temperature = GetTemperature()
        json_result = to_json(Self_Name, Temperature)
        print (json_result)
        client.publish(TOPIC, json_result)
        Temperature = GetTemperature()
        json_result = to_json(Self_Name, Temperature)
        print (json_result)
        client.publish(TOPIC, json_result)
        
except Exception as e:
    print("An error occurred:", e)
