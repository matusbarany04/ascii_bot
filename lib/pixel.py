
class Pixel:
    def __init__(self, x, y, bg, fg, char = ""):
        self.x = x
        self.y = y
        self.bg = bg
        self.fg = fg 
        self.char = char

    def __repr__(self):
        return f"Pixel(x={self.x}, y={self.y}, bg={self.bg}, fg={self.fg} char={self.char})"

    def serialize(self):
        return f"{self.x}{self.encode_y_coord()} {self.bg} {self.fg} {self.char if self.char else '" "'}"

    def from_serialized(serialized_pixel: str):
        arr = serialized_pixel.split(" ")

        x = int(arr[0][0:-2])
        y = int(Pixel.decode_y_coord(arr[0][-2:]))
        
        bg = int(arr[1])
        fg = int(arr[2])
        char = arr[3]

        return Pixel(x,y,bg,fg,char)

    def encode_y_coord(self):
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        if self.y < 0:
            raise ValueError("y coordinate must be a non-negative integer.")

        first_letter = alphabet[(self.y // 26) % 26]
        second_letter = alphabet[self.y % 26]         

        return first_letter + second_letter

    def decode_y_coord(serialized_y):
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        if len(serialized_y) != 2:
            raise ValueError("y coordinate must be 2 characters long.")

        y_fst = ord(serialized_y[0]) - ord('A')
        y_snd = ord(serialized_y[1]) - ord('A')    

        return y_fst * 26 + y_snd

        