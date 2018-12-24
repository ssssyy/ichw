"""我不知道为什么跑起来经常会有错误，输入框还会输入三遍。。。。。。"""

#!/usr/bin/env python3
"""wcount.py: count words from an Internet file.

__author__ = "SongYixin"
__pkuid__  = "1800011747"
__email__  = "1800011747@pku.edu.cn"
"""
import sys
import urllib.request
from urllib.request import urlopen
def gettxt():
    url=input()
    my_socket = urllib.request.urlopen(url)
    passage= my_socket.read().decode()
    my_socket.close()
    print("HTTP状态码：",my_socket.status)
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
    words=gettxt().split()
    b={}
    b=b.fromkeys(words)
    newwords=list(b.keys())
    for i in newwords:
        b[i]=words.count(i)
    return b

def sortandcount():
    nnwords={}
    nnworks=sorted(formdict().items(),key=lambda d:d[1],reverse=True)
    nnworks=dict(nnworks)
    del nnworks["-"]
    return nnworks

def main():
    gettxt()
    formdict()
    sortandcount()
    i=0
    s=input("你需要输出前多少个单词？")
    if s=="":
        s=10
    else:
        s=int(s)
    for m,n in sortandcount().items():
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
