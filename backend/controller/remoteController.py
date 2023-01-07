from queue import Queue
from threading import Thread

import json

class ControllerManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ControllerManager,cls).__new__(cls)
            cls._instance.__initialized = False
        return cls._instance

    def __init__(self):
        if self.__initialized:
            return
        self.__initialized = True
        self.remote_action_queue = Queue()
        self.worker = None
        print("init Called!!")

    def add(self, action):
        self.remote_action_queue.put(action)

        if (type(self.worker) is Thread and self.worker.is_alive() is False) or self.worker is None:
            self.worker = Thread(target=self.processActions, daemon=True)
            self.worker.start()
    
    def processActions(self):
        while self.remote_action_queue.qsize() > 0:
            action = self.remote_action_queue.get()
            print(json.dumps(action))