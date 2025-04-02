from lib.pixel import Pixel
from lib.color import get_hex_index, get_raw_color

# This class is only used for testing purposes
# and should not turned off when deploying
# There is a flag inside server.py to turn it on/off

class Rplace:

    def __init__(self, width = 4, height = 4):
        self.white = 15
        self.black = 0

        self.width = width
        self.height = height

        self.image_data = []
        for i in range(self.width * self.height):
            self.image_data.append(
                Pixel(
                    i % self.width, i // self.width, self.white, self.white
                )
            )

    def add_pixel(self, serialized_pixel):
        pixel = Pixel.from_serialized(serialized_pixel)
        print(pixel)
        self.image_data[int(pixel.y) * self.width + int(pixel.x)] = pixel
        
    def print_board(self):
        for i in range(len(self.image_data)):
            pixel = self.image_data[i]
            bg = int(pixel.bg)
            fg = int(pixel.fg)

            
            if bg == self.white and fg == self.white:
                print("█", end="")
            elif bg == self.white:
                print("▄", end="")
            elif fg == self.white:
                print("▀", end="")
            else:
                print(" ", end="")

            if pixel.x == self.width - 1:
                print("")
        print("")
