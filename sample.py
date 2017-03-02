from PIL import Image

IMG = input("input file: ")
WIDTH = 100
HEIGHT = 100
SAVE = input("save as: ")

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

def translate(r, g, b, alpha=256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b) 

    unit = (256.0 + 1) / length
    return ascii_char[int(gray/unit)]

image = Image.open(IMG)
image = image.resize((WIDTH, HEIGHT), Image.NEAREST)

txt = ""

for i in range(HEIGHT):
    for j in range(WIDTH):
        # if the output is too fat, comment the following line
        txt += ' '
        txt += translate(*image.getpixel((j, i)))
    txt += '\n'

f = open(SAVE, "w")
try:
    f.write(txt)
finally:
    f.close()
