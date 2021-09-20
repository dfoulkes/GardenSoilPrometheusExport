# simple inquiry example


from gatt import DeviceManager
from gatt import Device
import time

class BleDevice(Device):
    def connect_succeeded(self):
        super().connect_succeeded()
        print("[%s] Connected" % (self.mac_address))

    def connect_failed(self, error):
        super().connect_failed(error)
        print("[%s] Connection failed: %s" % (self.mac_address, str(error)))

    def disconnect_succeeded(self):
        super().disconnect_succeeded()
        print("[%s] Disconnected" % (self.mac_address))

    def services_resolved(self):
        super().services_resolved()

        # print("[%s] Resolved services" % (self.mac_address))
        # for service in self.services:
        #     print("[%s]  Service [%s]" % (self.mac_address, service.uuid))
        #     for characteristic in service.characteristics:
        #         print("[%s]    Characteristic [%s]" % (self.mac_address, characteristic.uuid))


class BleDeviceManager(DeviceManager):
    def device_discovered(self, device):
        print("Discovered [%s] %s" % (device.mac_address, device.alias()))
        
class SoilMonitor():

    def __init__(self, BleDevice):
     self._device = BleDevice
     self._currentValue = 0

    @property
    def bleDevice(self):
        return self._device
    
    def byte_array_to_int(value):
        value = bytearray(value)
        value = int.from_bytes(value, byteorder="little")
        return value

    def connectClient(self):
        self._device.connect()
        self._device.services_resolved()

    def disconnect(self):
        self._device.disconnect()        

    @property
    def CurrentValue(self):
      try:   
        self.connectClient()
        self._device.services_resolved()
        time.sleep(5)
        environmentService = next(service for service in device.services if service.uuid == "0000181a-0000-1000-8000-00805f9b34fb")
        soilCharacteristic = next(characteristic for characteristic in environmentService.characteristics if characteristic.uuid == "00002a6f-0000-1000-8000-00805f9b34fb")
        self._currentValue = byte_array_to_int(soilCharacteristic.read_value())
        self.disconnect()
        return self._currentValue
      except Exception:
        self.disconnect()  
        return -1        
    
# Reader("89:FB:C4:2E:BE:7E")
# print("Done.")

def byte_array_to_int(value):
    # Raw data is hexstring of int values, as a series of bytes, in little endian byte order
    # values are converted from bytes -> bytearray -> int
    # e.g., b'\xb8\x08\x00\x00' -> bytearray(b'\xb8\x08\x00\x00') -> 2232
    # print(f"{sys._getframe().f_code.co_name}: {value}")
    value = bytearray(value)
    value = int.from_bytes(value, byteorder="little")
    return value


manager = BleDeviceManager(adapter_name='hci0')

# device.connect()
# device.services_resolved()
# manager.start_discovery()
# atexit.register(device.disconnect_succeeded)

while True:

        # device_information_service = next(
        #     s for s in device.services
        #     if s.uuid == '00001801-0000-1000-8000-00805f9b34fb')
        manager.start_discovery()
        device = BleDevice(mac_address='89:FB:C4:2E:BE:7E', manager=manager)
        soilOne = SoilMonitor(device)
        print(soilOne.CurrentValue)
        device.disconnect()
        time.sleep(10)
        # firmware_version_characteristic = device_information_service.characteristics[0] 
        # environmentService = next(service for service in device.services if service.uuid == "0000181a-0000-1000-8000-00805f9b34fb")
        # soilCharacteristic = next(characteristic for characteristic in environmentService.characteristics if characteristic.uuid == "00002a6f-0000-1000-8000-00805f9b34fb")
        # print(byte_array_to_int(soilCharacteristic.read_value()))
       # print(byte_array_to_int(device.services[0].characteristics[0].read_value()))

#manager.start_discovery()
#manager.run()
# service = DiscoveryService()
# devices = service.discover(3)

# # nearby_devices = bluetooth.discover_devices(lookup_names=True)
# # print("Found {} devices.".format(len(nearby_devices)))

# for address, name in devices.items():
#        print("name: {}, address: {}".format(name, address))
 