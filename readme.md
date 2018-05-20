[TOC]

# 程序员的520怎么表白

## 照片墙
python picture_wall.py --help
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
![./out/img_ascii.png](./out/img_ascii.png)

### TODO
+ 字体大小不准确，待修正;
+ 子照片的处理方式有待提升，目前采用的只是根据字体像素透明度控制透明度，还可以抽象出来让用户选择控制方式～比如：
    * 根据字体像素透明度控制子图尺寸
    * 根据字体像素透明度控制子图形状
    * 根据字体像素透明度控制子图颜色亮度
    * 或者直接采用圆形裁剪子图

## 爱心情书








