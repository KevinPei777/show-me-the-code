from PIL import Image, ImageFont, ImageDraw

if __name__ == '__main__':
    image = Image.open(r'/media/kevinpei/ubuntu/PyPro/练习册/000/test.jpg')
    index = image.getbbox()  # (0, 0, 1215, 1271)

    # font
    font = ImageFont.truetype('consola.ttf', 100)
    # draw the image
    draw_image = ImageDraw.Draw(image)
    draw_image.text((190, -25), '4', fill=(255, 0, 0), font=font)

    image.save('result.jpg')
