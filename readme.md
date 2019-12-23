[TOC]

# 程序员的520怎么表白
原文地址： https: // github.com / HeLiangHIT / coders_love

# 一行python的表白
首先祭出绝招，用1行python表白：
```py
print('\n'.join([''.join([('I LOVE U'[(x - y) % 8] if ((x * 0.05)**2 + (y * 0.1)**2 - 1)**3 -
      (x * 0.05)**2 * (y * 0.1)**3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(15, -15, -1)]))
```
效果如下：
```
                 UI LOVE            LOVE UI L
            OVE UI LOVE UI LO   UI LOVE UI LOVE U
          LOVE UI LOVE UI LOVE UI LOVE UI LOVE UI L
         LOVE UI LOVE UI LOVE UI LOVE UI LOVE UI LOV
        LOVE UI LOVE UI LOVE UI LOVE UI LOVE UI LOVE
        OVE UI LOVE UI LOVE UI LOVE UI LOVE UI LOVE U
        VE UI LOVE UI LOVE UI LOVE UI LOVE UI LOVE UI
        E UI LOVE UI LOVE UI LOVE UI LOVE UI LOVE UI
         UI LOVE UI LOVE UI LOVE UI LOVE UI LOVE UI L
        UI LOVE UI LOVE UI LOVE UI LOVE UI LOVE UI LO
          LOVE UI LOVE UI LOVE UI LOVE UI LOVE UI LO
          OVE UI LOVE UI LOVE UI LOVE UI LOVE UI LO
          VE UI LOVE UI LOVE UI LOVE UI LOVE UI LOV
            UI LOVE UI LOVE UI LOVE UI LOVE UI LO
              LOVE UI LOVE UI LOVE UI LOVE UI LO
              OVE UI LOVE UI LOVE UI LOVE UI LO
                 UI LOVE UI LOVE UI LOVE UI L
                   LOVE UI LOVE UI LOVE UI
                    VE UI LOVE UI LOVE UI
                       I LOVE UI LOVE
                          VE UI LOV
                             I L
                              L
```
原理大概是：
```py
words, line = "I LOVE U", []
for y in range(15, -15, -1):
    line_c = []
    letters = ''
    for x in range(-30, 30):
        expression = ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3
        if expression <= 0:
            letters += words[(x-y) % len(words)]
        else:
            letters += ' '
    line_c.append(letters)
    line += line_c
print('\n'.join(line))
```

进一步可以制作成动画：
```py
def heart_text_animation(words="I LOVE U"):
  import time
  for c in words.split():
    line = []
    for y in range(15, -15, -1):
        line_c = []
        letters = ''
        for x in range(-30, 30):
            expression = ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3
            if expression <= 0:
                letters += c[(x-y) % len(c)]
            else:
                letters += ' '
        line_c.append(letters)
        line += line_c
    print('\n'.join(line))
    time.sleep(1)
```

# 粗糙的心形表白图像
```py
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0,2*np.pi, 0.1)
x = 16*np.sin(t)**3
y = 13*np.cos(t)-5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t)

plt.figure(figsize=(8,6), dpi=80, facecolor='white')
plt.plot(x,y,color='red')
plt.axis('off')
plt.fill(x,y,'hotpink')
plt.text(0, -0.4, 'ME & YOU', fontsize=36, fontweight='bold',
           color='black', horizontalalignment='center')
plt.show()
```
![./out/heart.png](./out/heart.png)
> 如果需要的话还可以进一步装饰


# 照片墙
依赖：
`pip install Image clize`

使用：
`python picture_wall.py --help`
```
Usage: picture_wall.py [OPTIONS] [text...]

生成照片墙

Arguments:
  text...                 Text of picture wall, if not defined this will generage a rectangle picture wall

Options:
  -s, --font-size=INT     font size of a clear value (default: 20)
  -e, --edge-len=INT      sub picture's egde length (default: 50)
  -w, --wall-width=INT    picture number of rectangle width (default: 20)
  -l, --wall-length=INT   picture number of rectangle length (default: 10)
  -d, --pic-dir=STR       picture's path (default: ./img)
  -o, --out-dir=STR       output dir (default: ./out/)
  -p, --font-path=STR     font path (default: ./demo.ttf)
  -m, --method=STR        decrator method, now accept 'alpha', 'size' (default: alpha)

Other actions:
  -h, --help              Show the help
```
for example:

`./picture_wall.py I Love U -s 30 -e 10`
![./out/I_LOVE_U.png](./out/I_LOVE_U.png)

`./picture_wall.py 我爱你 -s 30 -e 10`
![./out/我爱你.png](./out/我爱你.png)

如果指定为相册文件夹的话，将得到如下效果（文件夹下图片太多而且太大的话会比较慢）：
![./out/520.png](./out/520.png)

也可以选择尺寸的方式调整子图，例如: `python picture_wall.py 1314 -m size`
![./out/1314.png](./out/1314.png)



# TODO
+ 子照片的处理方式有待提升，目前采用的只是根据字体像素透明度控制透明度，还可以抽象出来让用户选择控制方式～比如：
    * 根据字体像素透明度控制子图形状
    * 根据字体像素透明度控制子图颜色亮度
    * 或者直接采用圆形裁剪子图

# 爱心情书
依赖：
`pip install jieba numpy pandas matplotlib wordcloud scipy wordcloud`

使用：
`python heart_cloud_word.py --help`
```
Usage: ./heart_cloud_word.py [OPTIONS] [par...]

生成文字云

Arguments:
  par...

Options:
  -t, --text-file=STR   text file that contain all you word (default: ./data/love_letter.txt)
  -s, --stop-file=STR   the stop word which can't be considered (default: ./data/stopwords.txt)
  -c, --color-img=STR   the color map img (default: ./data/pink.jpg)
  -m, --mask-file=STR   the mask img for the word
  -o, --out-file=STR    output file path which should with sufix of png/jpg... (default: ./out/word_cloud.png)
  -p, --font-path=STR   font path (default: ./demo.ttf)

Other actions:
  -h, --help            Show the help
```
for example:

`./heart_cloud_word.py`
![./out/word_cloud.png](./out/word_cloud.png)

# TODO
+ 增加背景照片和注释文字形成最终类似下图的效果
![./data/demo.jpg](./data/demo.jpg)


# 表白网站
1. 参考: http://www.jq22.com/yanshi1073  制作一个类似的网站，充分发挥想象~
2. 参考: https://github.com/Germey/ValentinesDay  绝对是真情流露，感人肺腑

欢迎关注作者，获取更新信息哦～

<img src="./owner.jpg" width = "300" height = "300" alt="关注作者" align=center />




