from pyhap.accessory import Accessory
from pyhap.const import CATEGORY_OUTLET

class Outlet(Accessory):
    category = CATEGORY_OUTLET

    def __init__(self, manufacturer="Python", serialNumber=None, callback=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_info_service(manufacturer=manufacturer, serial_number=serialNumber if serialNumber != None else 'INVALID SERIAL, INIT OBJECT WITH SERIAL')

        self.service = self.add_preload_service("Outlet")

        self.charecterOn = self.service.configure_char('On', setter_callback=self.setStatus if callback==None else callback)
        
    def setStatus(self, value):
        print(f"{self.display_name} turned {'on' if value else 'off'}")

if __name__ == "__main__":
    from pyhap.accessory_driver import AccessoryDriver
    driver = AccessoryDriver()
    driver.add_accessory(Outlet(driver=driver, display_name="Outlet"))
    driver.start()