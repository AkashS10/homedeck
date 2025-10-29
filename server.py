from datetime import datetime
from pyhap.accessory_driver import AccessoryDriver
from pyhap.accessory import Bridge
import subprocess
import threading
import socket

import webclient.manage as webClient
from sensors.light import Light

class Client:
    def __init__(self, clientSocket, address):
        self.s = clientSocket
        self.address = address
        logger.log(f"Client Connected ({self.address[0]}:{self.address[1]})")
        threading.Thread(target=self.recv, daemon=True).start()

    def recv(self):
        while True:
            try:
                data, addr = self.s.recvfrom(1024)
            except:
                self.disconnect()
                break
            if not data: 
                self.disconnect()
                break
            print(f"{self.address[0]}:{self.address[1]}: ", data)
    
    def disconnect(self):
        global clients
        logger.log(f"Client Disconnected ({self.address[0]}:{self.address[1]})")
        self.s.send(b"/b/")
        self.s.close()
        clients.remove(self)

class Logger:
    def __init__(self):
        pass
    
    def log(self, msg, error=False):
        print(f"[{'INFO' if not error else 'ERROR'}] @ {datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')} {msg}")

def handleConnections():
    c, addr = s.accept()
    clients.append(Client(c, addr))

def callback(value):
    for i in clients:
        if value:
            i.s.send(b"L1")
        else:
            i.s.send(b"L0")

# Init
clients = []
logger = Logger()
print("Press Ctrl+C to stop the server")
logger.log("Server started")

s = socket.socket()
s.bind(("0.0.0.0", 20119))
s.listen()

driver = AccessoryDriver()
bridge = Bridge(driver, display_name="HomeDeck Bridge")
sensors = []
l = Light("VIT", "ABCD1234", driver=driver, display_name="Light", callback=callback)
sensors.append(l)
for i in sensors:
    bridge.add_accessory(i)
driver.add_accessory(bridge)
threading.Thread(target=driver.start, daemon=True).start()

subprocess.Popen(["py", "manage.py", "runserver", "80"], cwd="./webclient", stdout=subprocess.PIPE)
threading.Thread(target=handleConnections, daemon=True).start()


while True:
    try:
        input()
    except KeyboardInterrupt:
        logger.log("Closing server")
        break

# Cleanup
for i in clients:
    i.disconnect()
driver.stop()