#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ref: https://github.com/Germey/TextImage
# usage: python text_background_image.py input_file output_file
# eg: python text_background_image.py ./data/mona-lisa.jpg ./out/text_background_image.jpg

from PIL import Image, ImageDraw, ImageFont
from sys import argv

# 字体大小
font_size = 10
# 字体间距，1 即间距正好为字体大小，紧凑排布，1.2 为字体大小的 1.2 倍
font_space = 1.2
# 绘制的文本
text = '我爱你'
# 字体文件的路径
font_file = './demo.ttf'

def draw_text_image(input_file, output_file):
    img_raw = Image.open(input_file)
    img_array = img_raw.load()
    img_new = Image.new('RGB', img_raw.size, (0, 0, 0))
    draw = ImageDraw.Draw(img_new)
    font = ImageFont.truetype(font_file, size=font_size)
    
    def character_generator(text):
        while True:
            for i in range(len(text)):
                yield text[i]
    
    ch_gen = character_generator(text)
    
    for y in range(0, img_raw.size[1], int(font_size * font_space)):
        for x in range(0, img_raw.size[0], int(font_size * font_space)):
            draw.text((x, y), next(ch_gen), font=font, fill=img_array[x, y], direction=None)
    
    img_new.convert('RGB').save(output_file)

if __name__ == '__main__':
    if len(argv) < 3:
        print("usage: python text_background_image.py input_file output_file")
    else:
        draw_text_image(argv[1], argv[2])
    
