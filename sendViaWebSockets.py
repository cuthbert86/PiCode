wifi_ssid = 'BB'
wifi_password = '6KH1jk1mn0s'
mqtt_server = b'e5d2174059b64286bd5f243dd055355a.s1.eu.hivemq.cloud'
mqtt_username = b"Cuthbert"
mqtt_password = b'Cbaines123!'
# TOPIC = "data1"

import time
import network
import urequests as requests
 
def connectWifi(ssid,passwd):
    global wlan
    wlan=network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.disconnect()
    wlan.connect(ssid,passwd)
    while(wlan.ifconfig()[0]=='0.0.0.0'):
        time.sleep(1)
    return True

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

# Wait for connect or fail
max_wait = 10
while max_wait > 0:

    if wlan.status() < 0 or wlan.status() >= 3:

        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)

# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('connected')
    status = wlan.ifconfig()
    print( 'ip = ' + status[0] )

while True:

# Do things here, perhaps measure something using a sensor?
  try:
  connectWifi(ssidRouter,passwordRouter)
  s = socket.socket()
  s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  s.connect((host,port))
  print("TCP Connected to:", host, ":", port)
  s.send('Hello')
  s.send('This is my IP.')
  while True:
    data = s.recv(1024)
    if(len(data) == 0):
      print("Close socket")
      s.close()
      break
    print(data)
    ret=s.send(data)
  except:
  print("TCP close, please reset!")
  if (s):
    s.close()
  wlan.disconnect()
  wlan.active(False)