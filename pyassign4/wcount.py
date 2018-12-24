"""注释：手动输入要打开的URL。这个统计里面the的数目偏少，但我在打开原网站以后用ctrl+f发现原网站的the真的只有700+，由于我没有去掉-这个连字符，所以
统计的每个单词的数量基本都偏少。如果在终端里面打不开，我也不知道该怎么办……因为我真的没能成功把存在本地的.py文件用cmd打开过……永远告诉我是语法错误。
我哭了，这个大作业我真的不太明白是怎么回事啊！！！！
"""

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
