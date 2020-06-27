# uTemp

### Temperature with uPython

Get the temp and humidity from my crawlspace with a DHT22, ESP8266 and Micro Python.  

### Requirements:

uPython 1.9 or higher, Adafruit Feather Huzzah board, DHT22 sensor  

### Setup:
Connect DHT22 sensor to your device with data on pin 4. 
Edit config.json to match your MQTT broker, ptopic is for publish, stopic is for subscribe.  
Load all .py files and config.json to a directory on your MicroPython device. 
Set up a subscriber to MQTT on your network.  

From the REPL on your device:  
`import utemp`  

`utemp.main()`  
