from pyhap.accessory import Accessory
from pyhap.const import CATEGORY_DOOR_LOCK
import time

class DoorLock(Accessory):
    category = CATEGORY_DOOR_LOCK

    def __init__(self, manufacturer="Python", serialNumber=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_info_service(manufacturer=manufacturer, serial_number=serialNumber if serialNumber != None else 'INVALID SERIAL, INIT OBJECT WITH SERIAL')

        self.service = self.add_preload_service("LockMechanism")

        self.charecterLock = self.service.configure_char('LockTargetState', setter_callback=self.setStatus)
        self.charecterLockState = self.service.get_characteristic("LockCurrentState")
    
    def setStatus(self, value):
        print(f"{self.display_name}: {value}")
        self.status = value
        self.charecterLockState.set_value(value)

if __name__ == "__main__":
    from pyhap.accessory_driver import AccessoryDriver
    driver = AccessoryDriver()
    driver.add_accessory(DoorLock(driver=driver, display_name="Door"))
    driver.start()