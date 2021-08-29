# Aim

So, I'm wanting to create a series of senors in my garden so I can track the soil moisture as well as other climate variables. 
they will work in client/server relationship and connected using Bluetooth. the Sensors will follow the [Bluetooth specifications](specificationrefs.bluetooth.com)
 to ensure compliance incase I was to change the system in the future.


Todo this, I plan to use a:

 1 x Raspberry Pi 4 
 > 1 x Arduino Nano 33 BLEs each with a Gravity: Analog Capacitive Soil Moisture Sensor


## Server (Raspberry Pi 4)
The server will have a custom python 3 service installed and Systemd service that will act a [prometheus](https://prometheus.io/) exporter. hosted on 8000
 