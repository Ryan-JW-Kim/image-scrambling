from PIL import Image, ImageDraw
import numpy as np
import sys

# file handle = sys.argv[1]

def dict_split(key_seg):

    commands_split = {}

    numbers = ""

    alpha = False # The key segment will always start with a number

    for char in key_seg:

        if char.isalpha() is False:

            numbers += char

        else:

            numbers = int(numbers)

            commands_split[char] = numbers

    return commands_split

def valid_key(key):

    return True

file_handle = "small_bird.jpeg" #sys.argv[1]

image_array = []

with Image.open(file_handle) as im:

    x_max, y_max = im.size

    for y in range(y_max):

        image_array.append([])

        for x in range(x_max):

            cord = x, y

            curr = im.getpixel(cord)
            image_array[y].append(curr)

rows = len(image_array)
cols = len(image_array[0])

array_red = []
array_green = []
array_blue = []

for row in range(rows):

    array_red.append([])
    array_green.append([])
    array_blue.append([])

    for col in range(cols):

        r, g, b = image_array[row][col]

        array_red[row].append((r,0,0))
        array_green[row].append((0,g,0))
        array_blue[row].append((0,0,b))

np_array_red = np.array(array_red)
np_array_green = np.array(array_green)
np_array_blue = np.array(array_blue)
 
red_image = Image.fromarray(np_array_red.astype(np.uint8))
blue_image = Image.fromarray(np_array_blue.astype(np.uint8))
green_image = Image.fromarray(np_array_green.astype(np.uint8))


scrambler_key = "12r54s83|12r|43s"#sys.argv[2]

if valid_key(scrambler_key):

    key_segments = scrambler_key.split("|")

    count = 0

    for seg in key_segments:

        if count == 0: #scrammbling red
            red_seg = dict_split(key_segments)

        elif count == 1: #scrammbling green
            green_seg = dict_split(key_segments)

        else: #scrammbling blue
            blue_seg = dict_split(key_segments)

        count += 1

    for key in red_seg.key():

    for key in green_seg.keys():

    for key in blue_seg.keys():

else:

    print("Key is not valid...")
#red_image.show()
#blue_image.show()
#green_image.show()
