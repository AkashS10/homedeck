from pyhap.accessory import Accessory
from pyhap.const import CATEGORY_LIGHTBULB

class ControllableLight(Accessory):
    category = CATEGORY_LIGHTBULB

    def __init__(self, manufacturer="Python", serialNumber=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_info_service(manufacturer=manufacturer, serial_number=serialNumber if serialNumber != None else 'INVALID SERIAL, INIT OBJECT WITH SERIAL')

        self.service = self.add_preload_service('Lightbulb', ["Brightness", "Hue", "Saturation"])

        self.charecterOn = self.service.configure_char('On', setter_callback=self.setStatus)
        self.charecterBrightness = self.service.configure_char('Brightness', setter_callback=self.setBrightness)
        self.charecterHue = self.service.configure_char('Hue', setter_callback=self.setHue)
        self.charecterSaturation = self.service.configure_char('Saturation', setter_callback=self.setSaturation)

    def setStatus(self, value):
        print(f"{self.display_name} turned {'on' if value else 'off'}")

    def setBrightness(self, value):
        print(f"{self.display_name} brightness: {value}")

    def setHue(self, value):
        print(f"{self.display_name} hue: {value}")

    def setSaturation(self, value):
        print(f"{self.display_name} saturation: {value}")

if __name__ == "__main__":
    from pyhap.accessory_driver import AccessoryDriver
    driver = AccessoryDriver()
    driver.add_accessory(accessory=ControllableLight(driver=driver, display_name='ControllableLight'))
    driver.start()
