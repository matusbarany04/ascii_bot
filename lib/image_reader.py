from PIL import Image
from .pixel import Pixel
from .color import get_hex_index

class ImageReader:


    def __init__(self, image_path):
        self.image_path = image_path
        self.width = None
        self.height = None

    
    def read_image(self):
        image = Image.open(self.image_path)


        pixels = image.load()

        output = [0] * (image.size[0] * image.size[1] // 2)

        self.width = image.size[0]
        self.height = image.size[1]

        for y in range(0, image.size[1], 2):
            for x in range(image.size[0]):
                # pixel width needs to be even
                r, g, b, a = pixels[x, y]
                r2, g2, b2, a2 = pixels[x, y + 1] 

                bg = get_hex_index(f"#{r2:02x}{g2:02x}{b2:02x}")
                fg = get_hex_index(f"#{r:02x}{g:02x}{b:02x}")

                output[x + image.size[0] * (y // 2)] = Pixel(x, y // 2, bg, fg, "▀")

        return output
