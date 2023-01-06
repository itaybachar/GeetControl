

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
        print("init Called!!")

    def add(self, action):
        return