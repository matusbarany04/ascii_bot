
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
        return f"{self.y}{self.encode_x_coord()} {self.bg} {self.fg} {self.char if self.char else '" "'}"

    def from_serialized(serialized_pixel: str):
        arr = serialized_pixel.split(" ")

        y = int(arr[0][0:-2])
        x = int(Pixel.decode_x_coord(arr[0][-2:]))
        
        bg = int(arr[1])
        fg = int(arr[2])
        char = arr[3]

        return Pixel(x,y,bg,fg,char)

    def encode_x_coord(self):
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        if self.x < 0:
            raise ValueError("y coordinate must be a non-negative integer.")

        first_letter = alphabet[(self.x // 26) % 26]
        second_letter = alphabet[self.x % 26]         

        return first_letter + second_letter

    def decode_x_coord(serialized_x):
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        if len(serialized_x) != 2:
            raise ValueError("y coordinate must be 2 characters long.")

        x_fst = ord(serialized_x[0]) - ord('A')
        x_snd = ord(serialized_x[1]) - ord('A')    

        return x_fst * 26 + x_snd

        