from flask import Flask, request, jsonify
from lib.pixel import Pixel
from lib.image_reader import ImageReader
from rplace import Rplace

virtual_rplace = True
image_name = "brandejs20.png"
x_offset = 10
y_offset = 0

app = Flask(__name__)

image_reader = ImageReader(f"./images/{image_name}")
pixel_data  = image_reader.read_image()

for pixel in pixel_data:
    pixel.x += x_offset
    pixel.y += y_offset

if virtual_rplace:
    rplace = Rplace(image_reader.width, image_reader.height//2)


def serialize_data(data):
    return [pixel.serialize() for pixel in data]

@app.route('/data')
def get_data():
    global pixel_data
    data = serialize_data(pixel_data)
    return jsonify(data)

@app.route('/put')
def put_pixel():
    if not virtual_rplace:
        return "error"
    pixel =request.args.get('pixel', None)
    if (pixel == None):
        return "error"
    rplace.add_pixel(pixel)
    rplace.print_board()
    return "ok"

if __name__ == '__main__':
    app.run(debug=True)