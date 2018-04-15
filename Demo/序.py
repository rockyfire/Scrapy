# _*_ coding:utf-8 _*_
__author__ = 'rockyfire'

import re

line = "rockyfire123"
line = "rockyxxxxxxxxxxxxxxxyzyyyyfire123"
line = "rockyfire789"
line = "你 好"

regex_str = "^r.*"
regex_str = "^r.*3$"
regex_str = ".*?(y.*?y).*"
regex_str = ".*x(y.+?y).*"
# group(1)最外面的括号包含的内容，
# group(2)次外面的括号左侧包含的内容，
# group(3)次外面的括号内侧包含的内容，
# group(4)次外面的括号右侧包含的内容，

regex_str = "(((rockyfire|rocckyfire)789)|(123|456))"
regex_str = "([\u4E00-\u9FA5].*)"
regex_str = "([\u4E00-\u9FA5]+)"

match_obj = re.match(regex_str, line)

# if match_obj:
#     print("----" + match_obj.group(1))

line = "xxx出生于2001年6月1日"
line = "xxx出生于2001/6/1"
line = "xxx出生于2001-6-1"
line = "xxx出生于2001-06-05"
# line = "xxx出生于2001-06"

regex_str=".*出生于?(\d+)[^\d]?(\d+)($|[^\d].*?(\d+))"

match_obj = re.match(regex_str, line)

if match_obj:
    print(match_obj.group(1)+"年"+match_obj.group(2)+"月")
    try:
        print(match_obj.group(4)+"日")
    except TypeError:
        print ("01日")