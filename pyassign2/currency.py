"""这是保底的代码"""

import sys
import urllib
import re

list1=['AED','AFN','ALL','AMD','ANG','AOA','ARS','AUD','AWG','AZN','BAM','BBD','BDT','BGN','BHD','BIF','BMD','BND','BOB','BRL','BSD','BTC',
'BTN','BWP','BYR','BZD','CAD','CDF','CHF','CLF','CLP','CNY','COP','CRC','CUC','CUP','CVE','CZK','DJF','DKK','DOP','DZD','EEK','EGP','ERN',
'ETB','EUR','FJD','FKP','GBP','GEL','GGP','GHS','GIP','GMD','GNF','GTQ','GYD','HKD','HNL','HRK','HTG','HUF','IDR','ILS','IMP','INR','IQD',
'IRR','ISK','JEP','JMD','JOD','JPY','KES','KGS','KHR','KMF','KPW','KRW','KWD','KYD','KZT','LAK','LBP','LKR','LRD','LSL','LTL','LVL','LYD',
'MAD','MDL','MGA','MKD','MMK','MNT','MOP','MRO','MTL','MUR','MVR','MWK','MXN','MYR','MZN','NAD','NGN','NIO','NOK','NPR','NZD','OMR','PAB',
'PEN','PGK','PHP','PKR','PLN','PYG','QAR','RON','RSD','RUB','RWF','SAR','SBD','SCR','SDG','SEK','SGD','SHP','SLL','SOS','SRD','STD','SVC',
'SYP','SZL','THB','TJS','TMT','TND','TOP','TRY','TTD','TWD','TZS','UAH','UGX','USD','UYU','UZS','VEF','VND','VUV','WST','XAF','XAG','XAU',
'XCD','XDR','XOF','XPD','XPF','XPT','YER','ZAR','ZMK','ZMW','ZWL']#用于检验货币名称是否合法的列表

#Part A 将用户输出转换为URL地址访问并获取字符串形式的汇率计算结果
def currency_response(currency_from, currency_to, amount_from):#这个函数可以将用户的输入转化为合法的URL地址并作为返回值
    a=currency_from
    b=currency_to
    c=amount_from#单纯只是为了好打代码一点所以换了个变量名
    url='http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='+a+'&to='+b+'&amt='+c
    return url

def get_json(url):
    from urllib.request import urlopen#访问并获取一段URL并获得它的字符串式返回
    doc = urlopen(url)
    docstr = doc.read()
    doc.close()
    json = docstr.decode('ascii')#这时的json变量已经与Part B函数的输入相同了
    return json

#Part B 对获取的字符串的解析，使其变为多个单词组
def first_inside_quotes(json):#这个函数可以获得第一个双引号中的内容而不包含该双引号
    #稍作修改，这个函数就可以抓取第n个双引号内的内容，虽然我在最后的exchange函数中并未用到它……
    if json.count('"')<2:#当输入的字符串总共拥有的双引号不足两个时，退出
        return
    a=re.findall(r'["](.*?)["]',json)#得到所有含引号的内容的一个列表
    first_part=a[0]
    return first_part

#首先将网页上获得的伪字典转变为字典的格式
true="true"
false="false"
def get_from(json):#通过字典的键值获得输出
    return eval(json)["from"]
def get_to(json):
    return eval(json)["to"]
def has_error(json):#在exchange函数中由于在获取用户输入后就已经用list检测了是否合法，故最终的程序不再需要这个函数，不过既然写了那还是保留吧
    a=eval(json)["success"]
    if a=="false":#当success的键值为False时，has_error函数返回True表明有错误；反之无错误
        return True
    return False

#Part C 对于获得的每个单词组中的数据的处理
def before_space(s):#该函数能够将一个字符串中位于第一个空格之前的内容输出为一个子字符串
    if " " not in s:
        return#排除掉输入字符串中不包含空格的情况
    s1=s.lstrip()#去掉该字符串最左边的空格，保证最终输出的子字符串是一个有实际含义的非空字符串
    ind=s1.find(" ")
    subs1=s1[:ind]
    return subs1
    
def after_space(s):#该函数能够将一个字符串中位于第一个空格之后的内容输出为一个子字符串
    if " " not in s:
        return#排除掉输入字符串中不包含空格的情况
    s1=s.lstrip()#作用同上
    ind=s1.find(" ")
    re_subs2=s1[ind:]
    subs2=re_subs2.lstrip()#如果该字符串的第1，2，3……n个空格连在一起，则去掉这些在新分割的字符串首的空格，使得带有多个连续空格的字符串也能获得想要的答案
    return subs2

#Part D 这是最后要实现的exchange函数了！！！！！胜利就在眼前！！！！！！(前面的都只是铺垫，这才是主函数)
currency_from=input("输入原货币的三位英文缩写")#获取用户的输入
currency_to=input("输入要转换至的货币的三位英文缩写")
amount_from=input("输入需要转换的原货币的数量")
    
def exchange(currency_from, currency_to, amount_from):
    if currency_from not in list1:#检验输入的原始货币名称是否符合规范
        print('{ "from" : "", "to" : "", "success" : false, "error" : "Source currency code is invalid." }')
        sys.exit()#退出，不再执行剩下的程序
    if currency_to not in list1:#检验输入的转换至的货币名称是否符合规范
        print('{ "from" : "", "to" : "", "success" : false, "error" : "Source currency code is invalid." }')
        sys.exit()#退出
    
    url=currency_response(currency_from, currency_to, amount_from)#将获得的URL对应字符串值赋给变量url
    json=get_json(url)#将获得的字符串储存在变量json中
    
    true="true"#这两行仅仅是为了处理字符串，无其他意义
    false="false"
    
    origin=get_from(json)
    new=get_to(json)
    
    num1=before_space(origin)#将解析得到的单词组转换为有实际意义的可读性高的文本并输出
    num2=before_space(new)
    currency1=after_space(origin)
    currency2=after_space(new)
    print("\t原货币："+currency1+"\n\t数量："+num1+"\n\n\t现货币："+currency2+"\n\t数量："+num2)

exchange(currency_from, currency_to, amount_from)

#Part E 测试函数部分
#接下来是测试函数部分，给定的参数为 USD CNY 4 可以测试以上出现的所有函数
def test_currency_response():#对第一个函数的测试
    assert(currency_response("USD", "CNY", "4")=='http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=USD&to=CNY&amt=4')

def test_get_json():#对第二个函数的测试
    assert(get_json('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=USD&to=CNY&amt=4')=='{ "from" : "4 United States Dollars", "to" : "27.4084 Chinese Yuan", "success" : true, "error" : "" }')

def test_first_inside_quotes():#对第三个函数的测试
    assert(first_inside_quotes('{ "from" : "4 United States Dollars", "to" : "27.4084 Chinese Yuan", "success" : true, "error" : "" }')=='from')
    
def test_get_from():#对第四个函数的测试
    assert(get_from('{ "from" : "4 United States Dollars", "to" : "27.4084 Chinese Yuan", "success" : true, "error" : "" }')=="4 United States Dollars")

def test_get_to():#对第五个函数的测试
    assert(get_to('{ "from" : "4 United States Dollars", "to" : "27.4084 Chinese Yuan", "success" : true, "error" : "" }')=="27.4084 Chinese Yuan")
    
def test_has_error():#对第六个函数的测试
    assert(has_error('{ "from" : "4 United States Dollars", "to" : "27.4084 Chinese Yuan", "success" : true, "error" : "" }')==False)
    
def test_before_space():#对第七个函数的测试
    assert(before_space("4 United States Dollars")=="4")
    
def test_after_space():#对第八个函数的测试
    assert(after_space("4 United States Dollars")=="United States Dollars")
    
def test_all():
    test_currency_response()
    test_get_json()
    test_first_inside_quotes()
    test_get_from()
    test_get_to()
    test_has_error()
    test_before_space()
    test_after_space()
    print("All tests passed!")
    
test_all()
