# Aim

So, I'm wanting to create a series of senors in my garden so I can track the soil moisture as well as other climate variables. 
they will work in client/server relationship and connected using Bluetooth. the Sensors will follow the [Bluetooth specifications](specificationrefs.bluetooth.com)
 to ensure compliance incase I was to change the system in the future.

 Why? as a fan of big data I want to be able to track the health of my garden overtime and aggregate this data in a graph. This could also one day be plugged into a automated valve to water the garden based off some predefined conditions however I will save that for
 version two. For now, the measurement of success is:
  
### Sensors

| Sensor      | Description                         |
| ----------- | ----------------------------------- |
| temperture  | measure temperture from outside     |
| humidity    | measure humidity from outside       | 
| pressure    | measure atmospheric preesure        | 
| soil        | measure the moisture from the soil  | 

### Prometheus Exporter 

These values should be captured from each node and presented as prometheus exporter.


## How ?

Todo this, I plan to use a:

 1 x Raspberry Pi 4 
 > 1 x Arduino Nano 33 BLEs each with a Gravity: Analog Capacitive Soil Moisture Sensor


## Server (Raspberry Pi 4)
The server will have a custom python 3 service installed and Systemd service that will act a [prometheus](https://prometheus.io/) exporter. hosted on 8000


## Document Version
   DELTA 0.0.1

# Author 
  Dan Foulkes
  danfoulkes@gmail.com

# License
MIT