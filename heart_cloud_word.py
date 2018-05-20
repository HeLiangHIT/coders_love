#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-20 18:26:50
# @Author  : He Liang (heianghit@foxmail.com)
# @Link    : https://github.com/HeLiangHIT
# ref      : https://github.com/amueller/word_cloud 
# usage: python heart_cloud_word.py --help

import jieba
import numpy
import pandas
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from scipy.misc import imread
from PIL import Image, ImageDraw
from wordcloud import ImageColorGenerator
from clize import Parameter, run


# jieba.load_userdict("./data/userdict.txt") # 加载自定义词库


def cut_file_text(text_file):
    # 读取文件内容并将其分词
    with open(text_file, encoding='utf8') as f:
        content = f.read()
    segs = jieba.cut(content) # 分词
    return [seg for seg in segs if len(seg) > 1 and seg != '\r\n'] # 拚弃标点符号和单字
# 读取内容
# segment = cut_file_text("./data/love_letter.txt")
# print(segment)

def word_statistics(seg, stop_words="./data/stopwords.txt"):
    # 1. 去除文本中不适合的词汇, 为了方便统计词频，我们把结果保存在pandas的 DataFrame 格式方便统计
    words_df = pandas.DataFrame({'segment':seg}) 
    # words_df.head()  # 查看大致内容
    stopwords = pandas.read_csv(stop_words, index_col=False, quoting=3, sep="\t", names=['stopword'], encoding="utf8")
    words_df = words_df[~words_df.segment.isin(stopwords.stopword)]
    # 2. 词频统计
    words_stat = words_df.groupby(by=['segment'])['segment'].agg({"count":numpy.size})
    words_stat = words_stat.reset_index().sort_values("count", ascending=False)
    # words_stat.to_csv('result.txt',sep='\t', encoding='utf-8')
    return words_stat
# word_stat = word_statistics(segment)
# print(word_stat.head(20000))

def _show_and_save_img(img, file_name = None):
    if file_name is not None:
        img.to_file(file_name)
    plt.axis("off")
    plt.imshow(img)
    plt.show()

# ref: https://github.com/amueller/word_cloud
def gen_word_cloud_rectangle(words_stat, font_path="./demo.ttf", background_color="white"):
    # 使用matplotlib和wordcloud工具来图形化显示上述的词频统计结果
    wordcloud = WordCloud(font_path=font_path, background_color=background_color)
    word_frequence = {x[0]: x[1] for x in words_stat.head(20000).values}
    # 最多显示20000个
    wordcloud = wordcloud.fit_words(word_frequence)
    return wordcloud
# img = gen_word_cloud_rectangle(word_stat)
# _show_and_save_img(img)


def gen_word_cloud_picture(words_stat, font_path="./demo.ttf", mask_file="./data/heart.jpg", 
        word_color_img="./data/pink.jpg", background_color="white"):
    # 自定义图像背景并将词云图形化输出
    mask_img = imread(mask_file)
    wordcloud = WordCloud(background_color=background_color, mask=mask_img, font_path=font_path)
    word_frequence = {x[0]: x[1] for x in words_stat.head(20000).values}
    wordcloud = wordcloud.fit_words(word_frequence)
    color_img = imread(word_color_img)
    mask_color = ImageColorGenerator(color_img)
    return wordcloud.recolor(color_func=mask_color)
# img = gen_word_cloud_picture(word_stat)
# _show_and_save_img(img, "./out/word_cloud.png")

def add_background(img, background="./data/background.jpg"):
    # 为词云添加背景图像
    new_img = img.to_image() # convert to Image
    background = Image.open(background)
    final_img = Image.blend(background, new_img, 1) 
    # 这样叠加是覆盖式的，需要专为numpy后再行判断叠加较好
    final_img.show()
    final_img.save("./out/word_cloud.png")

# add_background(img)

# ref: http://clize.readthedocs.io/en/stable/basics.html#collecting-all-positional-arguments
def main(*par, text_file:'t'="./data/love_letter.txt", stop_file:'s'="./data/stopwords.txt", color_img:'c'="./data/pink.jpg",
        mask_file:'m'="./data/heart.jpg", out_file:'o'="./out/word_cloud.png", font_path: 'p'='./demo.ttf',):
    '''生成文字云
    
    :param text_file: text file that contain all you word
    :param stop_file: the stop word which can't be considered
    :param color_img: the color map img
    :param mask_file: the mask img for the word
    :param out_file: output file path which should with sufix of png/jpg...
    :param font_path: font path
    '''
    segment = cut_file_text("./data/love_letter.txt")
    word_stat = word_statistics(segment)
    if mask_file is None:
        img = gen_word_cloud_rectangle(word_stat)
        _show_and_save_img(img, out_file)
    else:
        img = gen_word_cloud_picture(word_stat, font_path, mask_file, color_img)
        _show_and_save_img(img, out_file)



if __name__ == '__main__':
    run(main)



