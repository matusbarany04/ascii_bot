import requests
import time
import os
import re

debug = False
url = "http://127.0.0.1:5000"
wait_time = 1

def fetch_image():
    response = requests.get(url + "/data")

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

def put_pixel(pixel: str):
    # Pass pixel as a query parameter
    response = requests.get(f"{url}/put", params={"pixel": pixel})

    if response.status_code == 200:
        pass
    else:
        print(f"Failed to put data. Status code: {response.status_code}")

def sanitize_input(serialized_pixel):
    sanitized_pixel = re.sub(r"[^a-zA-Z0-9 ▀]", "", serialized_pixel)
    return sanitized_pixel


def write_pixel(serialized_pixel):
    sanitized_pixel = sanitize_input(serialized_pixel)

    pixel_command = f"perl artscii_command/artscii put {sanitized_pixel}"

    print(pixel_command)

    if debug:
        put_pixel(pixel)
    else:
        os.system(pixel_command)  


def get_pixel_from_canvas(x, y):
    pass

def is_pixel_correct(x, y, bg, fg):
    return True
    pass


#### TODO ####
#  - smart drawing algorithm -
#  dont draw on pixels which are the 
#  correct color already
#
# - sync with other users -
#  while drawing for example an animation, there's
#  a need for syncing with other users

while True:

    data = fetch_image()
    
    wrote = False
    for pixel in data:
        # if not is_pixel_correct(pixel.x, pixel.y, pixel.bg, pixel.fg):
        #     continue
        wrote = True
        write_pixel(pixel)
        time.sleep(wait_time)

    if not wrote:
        # this prevents death loop 
        # when every pixel is correct
        time.sleep(5) 
    time.sleep(1)
