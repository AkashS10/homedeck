from pyhap.accessory import Accessory
from pyhap.const import CATEGORY_FAN

class Fan(Accessory):
    category = CATEGORY_FAN

    def __init__(self, manufacturer="Python", serialNumber=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_info_service(manufacturer=manufacturer, serial_number=serialNumber if serialNumber != None else 'INVALID SERIAL, INIT OBJECT WITH SERIAL')

        self.service = self.add_preload_service("Fan", ["RotationSpeed"])
        self.charecterOn = self.service.configure_char('On', setter_callback=self.setStatus)
        self.charecterSpeed = self.service.configure_char('RotationSpeed', setter_callback=self.setSpeed)
    
    def setStatus(self, value):
        print(f"{self.display_name} turned {'on' if value else 'off'}")

    def setSpeed(self, value):
        print(f"{self.display_name} speed: {value}")

if __name__ == "__main__":
    from pyhap.accessory_driver import AccessoryDriver
    driver = AccessoryDriver()
    driver.add_accessory(Fan(driver=driver, display_name="Fan"))
    driver.start()
