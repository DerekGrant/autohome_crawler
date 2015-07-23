#coding=utf-8
import urllib
import re

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r' src="(http://.*\.jpg)" '
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    print imglist
    x = 0
    for imgurl in imglist:

        urllib.urlretrieve(imgurl,'%s.jpg' % x)
        x+=1

    reg = r' src="(http://.*\.png)" '
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    print imglist
    x = 0
    for imgurl in imglist:

        urllib.urlretrieve(imgurl,'%s.png' % x)
        x+=1


html = getHtml("http://www.juhe.cn/docs")

print getImg(html)
