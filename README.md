# spiders
#一些之前写过的爬虫，还有一些未完成的爬虫例如:汉服绘，奇漫屋，七麦数据等等
其中带反爬的大多数是扣js实现的
通过以下代码，调用js
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
# 使用execjs时可能会遇到乱码报错，你可以加上面三句话处理掉报错，也可以更改源文件
import execjs
with open('js.js', 'r') as f:
    text = f.read()
    jst = execjs.compile(text)
有一些没解决的还请各位大佬指点指点!
