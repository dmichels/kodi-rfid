import keyboard
import time

class RfidScanner:

    def __init__(self, scan_hook):
        self.scan_hook = scan_hook
        self.scanned_code = ""
        self.last_scan_time = 0
        keyboard.on_press(self.key_press)

    def key_press(self, event):
        if event.scan_code >= 2 and event.scan_code <= 11:
            self.scanned_code += event.name

        if event.scan_code == 28 and len(self.scanned_code) > 0 and time.time() - self.last_scan_time > 15:
            self.last_scan_time = time.time()
            self.scan_hook(self.scanned_code)
            self.scanned_code = ""


if __name__ == "__main__":

    def on_scan(code):
        print("scanned: %s" % code)
    
    RfidScanner(on_scan)

    while True:
        time.sleep(1)