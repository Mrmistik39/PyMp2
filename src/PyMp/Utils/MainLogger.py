import sys
import threading
import datetime


class MainLogger(threading.Thread):

    def __init__(self):
        super().__init__()
        self.date = datetime.datetime.today()

    def Warning(self, text):
        print(f'[{self.date.strftime("%H:%M:%S")}] [Warning]: {text}')

    def Info(self, text):
        print(f'[{self.date.strftime("%H:%M:%S")}] [Info]: {text}')

    def error(self, text):
        print(f'[{self.date.strftime("%H:%M:%S")}] [ERROR]: {text}')

    def run(self):
        for line in sys.stdin:
            print(line)
