#!/usr/bin/env python3
"""wcount.py: count words from an Internet file.

__author__ = "SongYixin"
__pkuid__  = "1800011747"
__email__  = "1800011747@pku.edu.cn"
"""
import sys
import urllib.request
from urllib.request import urlopen

#初始化全局变量
passage=""
b=""
nnworks=""
s=""

def gettxt():
    global passage
    if len(sys.argv) >=2:
        url=sys.argv[1]
    my_socket = urllib.request.urlopen(url)
    passage= my_socket.read().decode()
    my_socket.close()
    print("HTTP状态码：",my_socket.status)
    #处理几个状态码
    if my_socket.status == 200:
        print("打开请求成功！ 200 OK")
    elif my_socket.status == 404:
        print("这个页面找不到了！404 Not Found")
    elif my_socket.status == 500 or 501 or 502 or 503 or 504 or 505:
        print("网络或服务器错误！")
    for a in '~!@#$%^&*()_+"{}[]|/,:?.<>?;':
        passage=passage.replace(a,"")
    return passage

def formdict():
    global passage
    global b
    #将处理过的文本处理为单个单词
    words=passage.split()
    nwords=list(map(lambda x:x.lower(),words))
    #自动填成字典
    b={}
    b=b.fromkeys(nwords)
    newwords=list(b.keys())
    for i in newwords:
        b[i]=nwords.count(i)
    return b

def sortandcount():
    global b
    global nnworks
    #字典按值排序
    nnwords={}
    nnworks=sorted(b.items(),key=lambda d:d[1],reverse=True)
    nnworks=dict(nnworks)
    del nnworks["-"]
    return nnworks

def main():
    global nnworks
    global s
    gettxt()
    formdict()
    sortandcount()
    i=0
    #从用户输入中获取参数
    if len(sys.argv) == 3:
        s=int(sys.argv[2])
    elif len(sys.argv) == 2:
        s=10
    for m,n in nnworks.items():
        if i < s:
            print(format(m),format(n))
            i+=1
        else:
            break

if __name__ == '__main__':
    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)
    main()
