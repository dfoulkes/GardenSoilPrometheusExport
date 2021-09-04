#include <ArduinoBLE.h>
#include <Arduino_LSM9DS1.h> // even if we aren't using the accelerometer, its library needs to be included?
#include <Arduino_HTS221.h>

int humX = 1;
int mositure = 1;
float x, y;

BLEService environmentService("181A");
BLEUnsignedIntCharacteristic moistureCharacteristic("2A6F", BLERead | BLENotify);

void read_temphum() {
 mositure = analogRead(A0);
}

void setup() {
 
  Serial.begin(9600);
  while (!Serial);
  pinMode(LED_BUILTIN,OUTPUT); // Ready the onboard LED

  // BLE error catching
  if (!BLE.begin()){
    // Serial.println("BLE failed to initiate");
    while(1);
  }
  BLE.setLocalName("arduinoTsensor");
  BLE.setAdvertisedService(environmentService);
  environmentService.addCharacteristic(moistureCharacteristic);
  BLE.addService(environmentService);
  moistureCharacteristic.writeValue(mositure);
  BLE.advertise();
  Serial.println("Bluetooth device now active, waiting for connect...");
}

void loop() {
  BLEDevice central = BLE.central();
  if (central){
    Serial.print("Connected to central: ");
    Serial.println(central.address());
    digitalWrite(LED_BUILTIN, HIGH);
    
    while (central.connected()){
      delay(1000);
      read_temphum();
      moistureCharacteristic.writeValue(mositure);
    }

    digitalWrite(LED_BUILTIN,LOW);
    Serial.print("Disconnected from central: ");
    Serial.println(central.address());
  }

}