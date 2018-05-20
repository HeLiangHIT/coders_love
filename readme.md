[TOC]

# 程序员的520怎么表白

## 照片墙
依赖：
`pip install Image clize`

使用：
`python picture_wall.py --help`
```
Usage: ./picture_wall.py [OPTIONS] [text...]

生成照片墙

Arguments:
  text...                 Text of picture wall, if not defined this will generage a rectangle picture wall

Options:
  -s, --font-size=INT     font size of a clear value (default: 20)
  -e, --edge-len=INT      sub picture's egde length (default: 50)
  -w, --wall-width=INT    picture number of rectangle width (default: 20)
  -l, --wall-length=INT   picture number of rectangle length (default: 10)
  -d, --pic-dir=STR       picture's path (default: ./img)
  -o, --out-dir=STR       output dir (default: ./out)
  -p, --font-path=STR     font path (default: ./demo.ttf)

Other actions:
  -h, --help              Show the help
```
for example:

`./picture_wall.py I Love U -s 30 -e 10`
![./out/I_LOVE_U.png](./out/I_LOVE_U.png)

`./picture_wall.py 我爱你 -s 30 -e 10`
![./out/我爱你.png](./out/我爱你.png)

### TODO
+ 子照片的处理方式有待提升，目前采用的只是根据字体像素透明度控制透明度，还可以抽象出来让用户选择控制方式～比如：
    * 根据字体像素透明度控制子图尺寸
    * 根据字体像素透明度控制子图形状
    * 根据字体像素透明度控制子图颜色亮度
    * 或者直接采用圆形裁剪子图

## 爱心情书
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
![./out/word_cloud.png]

### TODO
+ 增加背景照片和注释文字形成最终类似下图的效果
![./data/demo.jpg](./data/demo.jpg)




