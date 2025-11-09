from pyhap.accessory import Accessory
from pyhap.const import CATEGORY_SENSOR
import time

class TemperatureSensor(Accessory):
    category = CATEGORY_SENSOR

    def __init__(self, manufacturer="Python", serialNumber=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_info_service(manufacturer=manufacturer, serial_number=serialNumber if serialNumber != None else 'INVALID SERIAL, INIT OBJECT WITH SERIAL')

        self.service = self.add_preload_service("TemperatureSensor")
        self.setTemperature = lambda temp: self.service.get_characteristic("CurrentTemperature").set_value(temp)

if __name__ == "__main__":
    from pyhap.accessory_driver import AccessoryDriver
    driver = AccessoryDriver()
    t = TemperatureSensor(driver=driver, display_name="Temperature Sensor")
    t.setTemperature(15)
    driver.add_accessory(t)
    driver.start()