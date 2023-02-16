from queue import Queue
from threading import Thread
from time import sleep

import pynput.keyboard as kbctl
import pynput.mouse as msctl

import json

keyboard = kbctl.Controller()
mouse = msctl.Controller()


class ControllerManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ControllerManager, cls).__new__(cls)
            cls._instance.__initialized = False
        return cls._instance

    def __init__(self):
        if self.__initialized:
            return
        self.__initialized = True
        self.remote_action_queue = Queue()
        self.worker = None

    def add(self, action):
        self.remote_action_queue.put(action)

        if (
            type(self.worker) is Thread and self.worker.is_alive() is False
        ) or self.worker is None:
            self.worker = Thread(target=self.__processActions, daemon=True)
            self.worker.start()

    def __processActions(self):
        while self.remote_action_queue.qsize() > 0:
            instruction = self.remote_action_queue.get()
            action = instruction.get("action", None)
            if action == "keyboard":
                typeKey(instruction["key"])
            elif action == "volume":
                changeVolume(instruction["change"])
            elif action == "mouse-click":
                mouseClick(instruction["btn"])
            elif action == "mouse-move":
                mouseMove(instruction["dx"], instruction["dy"], instruction["force"])
            elif action == "mouse-scroll":
                scrollWheel(instruction["direction"])
            # print(json.dumps(instruction))


def typeKey(key):
    try:
        if key == " ":
            keyboard.tap(kbctl.Key.space)
        elif key == "Enter":
            keyboard.tap(kbctl.Key.enter)
        elif key == "Backspace":
            keyboard.tap(kbctl.Key.backspace)
        else:
            keyboard.tap(key)
    except:
        pass


def changeVolume(change):
    try:
        if change == "UP":
            keyboard.tap(kbctl.Key.media_volume_up)
        elif change == "DOWN":
            keyboard.tap(kbctl.Key.media_volume_down)
    except:
        pass


def mouseClick(btn):
    try:
        if btn == "left":
            mouse.click(msctl.Button.left, 1)
        elif btn == "right":
            mouse.click(msctl.Button.right,1)
    except:
        pass


def mouseMove(dx, dy, force):
    try:
        # Convert POST values to floats
        dx = float(dx)
        dy = float(dy)
        force = float(force)

        # Get current Mouse position
        mouse.move(dx * force, dy * force)
        sleep(0.001)
    except:
        pass


# UP/ DOWN
def scrollWheel(direction):
    try:
        if direction == "UP":
            mouse.scroll(0, 2)
        elif direction == "DOWN":
            mouse.scroll(0, -2)
    except:
        pass
