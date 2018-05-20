#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-20 18:26:50
# @Author  : He Liang (heianghit@foxmail.com)
# @Link    : https://github.com/HeLiangHIT
# usage: python heart_cloud_word.py --help

import jieba    #中文分词大名鼎鼎的jieba包
import numpy    #numpy计算包
import codecs   #codecs提供的open方法来指定打开的文件的语言编码，它会在读取的时候自动转换为内部unicode 
import pandas   #数据分析包
import matplotlib.pyplot as plt #绘图包
from wordcloud import WordCloud #词云包
from scipy.misc import imread
from wordcloud import ImageColorGenerator

'''读取聊天记录'''
file=codecs.open("kwy.txt",'r','utf-8')#读取文本使用codecs包可以先通过设置文件的编码，对文件进行读入，这样子就不用边读遍转码了，非常实用。
content=file.read()
file.close()
segment=[]
jieba.load_userdict("userdict.txt")#为了提高分词的准确度，我们最好寻找我们分词的词库
segs=jieba.cut(content) #切词，“么么哒”才能出现
for seg in segs:
    #一个字的词，基本上算是无用的词，或者说是标点符号，因此这里直接抛弃了
    if len(seg)>1 and seg!='\r\n':
        segment.append(seg)


'''想要生成一个较为理想的词云，分词的内容质量很重要，那么必须要做的一步就是要去除文本中的“噪音”，通常的实现方法是：先定义一个停用词集，然后利用停用词集对上面的文本分词全集进行过滤，最后形成一个有效词集。
这里要给大家一句非常重要的温馨提醒，我们希望每一位同学在处理相关数据时都能秉持公正客观真实的原则，但如果你最终导出的结果与你预期的“甜蜜”记录并不符合，比如出现了“多喝热水”等尴尬的词语，那么在去听用词中，适当的抹去这样的小细节来避免明年一个人过节，也是可以理解的。'''
words_df=pandas.DataFrame({'segment':segment})# 为了方便统计词频，我们把结果保存在pandas的DataFrame中。
words_df.head()
# 移除停用词
stopwords=pandas.read_csv("stopwords.txt",index_col=False,quoting=3,sep="\t",names=['stopword'],encoding="utf8")
words_df=words_df[~words_df.segment.isin(stopwords.stopword)]


'''词频统计。我们需要统计有效词集中每个词的出现次数，然后按照次数从多到少进行排序。其中统计使用groupby函数，排序使用sort函数'''
words_stat=words_df.groupby(by=['segment'])['segment'].agg({"计数":numpy.size})
words_stat=words_stat.reset_index().sort(columns="计数",ascending=False)
# print words_stat  #打印统计结果
words_stat.to_csv('result.txt',sep='\t', encoding='utf-8')


'''睛之笔：数据图形化显示。有了强有力的工具包，这些工作都是分分钟就可以搞定。我们使用matplotlib和wordcloud工具来图形化显示上述的词频统计结果。'''
# wordcloud=WordCloud(font_path="simhei.ttf",background_color="black")
# wordcloud=wordcloud.fit_words(words_stat.head(20000).itertuples(index=False))
# plt.imshow(wordcloud)
# plt.show()

'''当然还可以把图形呈现玩得再酷炫一些，自定义一个心形图像背景并将词云图形化输出。将生成的图形以本地图片的形式生成并打开显示。'''
bimg=imread('heart.jpg')
wordcloud=WordCloud(background_color="white",mask=bimg,font_path=u'汉仪秀英体简.ttf')
wordcloud=wordcloud.fit_words(words_stat.head(20000).itertuples(index=False))
# wordcloud=wordcloud.fit_words(words_stat.head(20000).itertuples(index=True))
plt.axis("off")
cimg = imread('color.jpg')
bimgColors=ImageColorGenerator(cimg)
plt.imshow(wordcloud.recolor(color_func=bimgColors))#颜色映射
# plt.imshow(wordcloud)#随机颜色
plt.show()



