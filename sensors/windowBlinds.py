from pyhap.accessory import Accessory
from pyhap.const import CATEGORY_WINDOW

class windowBlinds(Accessory):
    category = CATEGORY_WINDOW

    def __init__(self, manufacturer="Python", serialNumber=None, callback=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_info_service(manufacturer=manufacturer, serial_number=serialNumber if serialNumber != None else 'INVALID SERIAL, INIT OBJECT WITH SERIAL')

        self.service = self.add_preload_service("Window")

        self.charecterOpen = self.service.configure_char('TargetPosition', setter_callback=self.setStatus)
        self.charecterWindowState = self.service.get_characteristic("CurrentPosition")
    
    def setStatus(self, value):
        print(f"{self.display_name}: {value}")
        self.status = value
        self.charecterWindowState.set_value(value)


if __name__ == "__main__":
    from pyhap.accessory_driver import AccessoryDriver
    driver = AccessoryDriver()
    driver.add_accessory(windowBlinds(driver=driver, display_name="Blinds"))
    driver.start()