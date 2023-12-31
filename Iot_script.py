import serial
import re
import urllib.request
import json
import requests
ArduinoSerial = serial.Serial('COM3', 9600)



def temperature():
    ammonia = None
    temperature_value = None
    humidity_value = None

    while True:
        if ArduinoSerial.inWaiting() > 0:
            mydata = ArduinoSerial.readline().decode('UTF-8')
            print(mydata)

            ammonia_match = re.search(r'Ammonia(\d+)', mydata)
            print("Abhi")

            res = [int(i) for i in mydata.split() if i.isdigit()]
            print(res)
            print(res[1])
            f=urllib.request.urlopen('https://api.thingspeak.com/update?api_key=JPSCXFRCRQ2S5EZU&field1='+str(res[0]))
            print(f)
            temperature_match = re.search(r'Temperature:\s*(\d+)\s*C', mydata)
            f=urllib.request.urlopen('https://api.thingspeak.com/update?api_key=4WAPZSL6Z335WNI0&field2='+str(res[1]))
            print(f)
            print("Abhi")
            print(res[1])
            humidity_match = re.search(r'Humidity:\s*(\d+)', mydata)
            f=urllib.request.urlopen('https://api.thingspeak.com/update?api_key=JPSCXFRCRQ2S5EZU&field3='+str(res[2]))
            print(f)
            return

            if ammonia_match:
                ammonia = int(ammonia_match.group(1))
            if temperature_match:
                temperature_value = int(temperature_match.group(1))
            if humidity_match:
                humidity_value = int(humidity_match.group(1))

            if ammonia is not None and temperature_value is not None and humidity_value is not None:

                return ammonia, temperature_value, humidity_value



a, b, c = temperature()  
print('Ammonia: ' + str(a) + ', Temperature: ' + str(b) + '°C, Humidity: ' + str(c))
