import cv2


class Mouse:
    def __init__(self, screen):
        self.screen = screen
        self.x = self.y = 0

    def start_record(self):
        cv2.setMouseCallback(self.screen, self.__xy)

    def __xy(self, event, x, y, flags, param):
         self.x, self.y = x, y
