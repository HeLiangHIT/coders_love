#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-10 15:16:09
# @Author  : He Liang (heianghit@foxmail.com)
# @Link    : https://github.com/HeLiangHIT

from PIL import Image, ImageDraw, ImageFont
import functools


effects_func = {}
def effects(name):
    '''收集子图装饰效果函数'''
    def wraper(func):
        effects_func[name] = func
        return func
    return wraper


@effects('alpha')
def trans_alpha(img, pixel):
    '''根据rgba的pixel调节img的透明度'''
    _, _, _, alpha = img.split()
    alpha = alpha.point(lambda i: pixel[-1])
    img.putalpha(alpha)
    return img


@effects('size')
def trans_size(img, pixel):
    '''根据rgba的pixel调节img的尺寸并放置在中心，输出尺寸不能变'''
    linear = lambda x, y: int(x * y / 256)
    tar_len, tar_width = linear(img.size[0], pixel[-1]), linear(img.size[1], pixel[-1])
    n_img = Image.new('RGBA', img.size)
    if tar_len > 1 and tar_width > 1:
        s_img = img.resize((tar_len, tar_width), Image.ANTIALIAS)
        start_pos = lambda l, s: int(l / 2 - s / 2)
        left, top = start_pos(img.size[0], s_img.size[0]), start_pos(img.size[1], s_img.size[1])
        n_img.paste(s_img, (left, top))
    return n_img


