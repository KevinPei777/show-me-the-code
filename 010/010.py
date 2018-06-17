from PIL import Image, ImageFont, ImageDraw
import string
import random


def get_random_string():
    all_string = string.ascii_letters
    random_string = ''.join(random.choices(all_string, k=4))
    return random_string


def get_bg_random():
    return random.randint(0, 196), random.randint(0, 196), random.randint(0, 196)


width = 90
height = 40
image = Image.new('RGB', (width, height), get_bg_random())

# 绘制字体
string_font = ImageFont.truetype('consola.ttf', 35, )
string_text = get_random_string()
draw_string = ImageDraw.Draw(image)
for i in range(len(string_text)):
    draw_string.text((5+20 * i, random.randint(0, height-40)), string_text[i], font=string_font)

# 绘制点数
draw_dot = ImageDraw.Draw(image)
for i in range(width * height // 3):
    draw_dot.point((random.randint(0, width), random.randint(0, height)), fill=get_bg_random())

image.save('test.jpg')
