from machine import Pin, I2C
import network
import utime
from umqtt.simple import MQTTClient
import usocket
from time import time, sleep
from machine import Pin
import micropython
import ustruct as struct

SSID = 'BB'
PASSWORD = b'6KH1jk1mn0s'
adcpin = 4
sensor = machine.ADC(adcpin)
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.config(pm = 0xa11140) # Diable powersave mode
wlan.connect(SSID, PASSWORD)

max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
        max_wait -= 1
        print('waiting for connection...')
        utime.sleep(1)

#Handle connection error
    if wlan.status() != 3:
        raise RuntimeError('wifi connection failed')
    else:
        print('connected')
        status = wlan.ifconfig()
        print('ip = ' + status[0])


def ReadTemperature(temp):
    adc_value = sensor.read_u16()
    volt = (3.3/65535) * adc_value
    temperature = 27 - (volt - 0.706)/0.001721
    temp = round(temperature, 1)
    return temp


def connectMQTT():
    client = MQTTClient(client_id=b"kudzai_raspberrypi_picow")
    server=b"8fbadaf843514ef286a2ae29e80b15a0.s1.eu.hivemq.cloud"
    port=8883
    user=b"mydemoclient"
    password=b"passowrd"
    keepalive=7200
    ssl=True
    ssl_params={'server_hostname':'8fbadaf843514ef286a2ae29e80b15a0.s1.eu.hivemq.cloud'}
    

    client.connect()
    return client


def publish(topic, value):
    print(topic)
    print(value)
    client.publish(topic, value)
    print("publish Done")


while True:
#Read sensor data
    temperature = ReadTemperature(temp)[0]

    print(temperature)
#publish as MQTT payload
    publish('pico/temperature', temperature)

#delay 5 seconds
    utime.sleep(10)
