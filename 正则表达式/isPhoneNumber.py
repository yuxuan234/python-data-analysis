#! python3
# -*- coding: UTF-8 -*-

import re

"""
函数说明:main函数

Parameters:
    re.compile传入一个字符串值，表示正则表达式，它将返回一个Regex 模式对象（或者就简称为Regex 对象）
    search()方法查找传入的字符串
Returns:
    无
Modify:
    2020-06-27
"""

# 匹配Regex 对象
# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')

# 利用括号分组
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)

# 用管道匹配多个分组
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group())

mo2 = heroRegex.search('Tina Fey and Batman.')
print(mo2.group())


batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))

# 用问号实现可选匹配
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
print(mo1.group())

mo2 = phoneRegex.search('My number is 555-4242')
print(mo2.group())


# 用星号匹配零次或多次
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())

# 用加号匹配一次或多次
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwowowowoman')
print(mo2.group())

mo3 = batRegex.search('The Adventures of Batman')
print(mo3 is None)

# 用花括号匹配特定次数
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())

mo2 = haRegex.search('Ha')
print(mo2 is None)

# 花括号的贪心形式和非贪心形式之间的区别：
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())

# findall()方法
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # has no groups
mo = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo)

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')  # has no groups
mo = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo)

# 字符分类
xmasRegex = re.compile(r'\d+\s\w+')
mo = xmasRegex.findall(
    '12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids,'
    ' 7swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(mo)


# 建立自己的字符分类
vowelRegex = re.compile(r'[aeiouAEIOU]')
mo = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(mo)

consonantRegex = re.compile(r'[^aeiouAEIOU]')
mo = consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')
print(mo)

# 插入字符和美元字符
beginsWithHello = re.compile(r'^Hello')
mo = beginsWithHello.search('Hello world!')
print(mo)
mo1 = beginsWithHello.search('He said hello.') is None
print(mo1)

endsWithNumber = re.compile(r'\d$')
mo = endsWithNumber.search('Your number is 42')
print(mo)
mo1 = endsWithNumber.search('Your number is forty two.') is None
print(mo1)


wholeStringIsNum = re.compile(r'^\d+$')
mo = wholeStringIsNum.search('1234567890')
print(mo)
mo1 = wholeStringIsNum.search('12345xyz67890') is None
print(mo1)
mo2 = wholeStringIsNum.search('12 34567890') is None
print(mo2)

# 通配字符
atRegex = re.compile(r'.at')
mo = atRegex.findall('The cat in the hat sat on the flat mat.')
print(mo)

# 用点-星匹配所有字符
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))
print(mo.group(2))

nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

# 用句点字符匹配换行
noNewlineRegex = re.compile('.*')
mo = noNewlineRegex.search(
    'Serve the public trust.\nProtect the innocent.nUphold the law.').group()
print(mo)

newlineRegex = re.compile('.*', re.DOTALL)
mo = newlineRegex.search(
    'Serve the public trust.\nProtect the innocent.nUphold the law.').group()
print(mo)


# 不区分大小写的匹配
robocop = re.compile(r'robocop', re.I)
mo = robocop.search('RoboCop is part man, part machine, all cop.').group()
print(mo)
mo1 = robocop.search('ROBOCOP protects the innocent.').group()
print(mo1)
mo2 = robocop.search(
    'Al, why does your programming book talk about robocop so much?').group()
print(mo2)

# 用sub()方法替换字符串
namesRegex = re.compile(r'Agent \w+')
mo = namesRegex.sub(
    'CENSORED',
    'Agent Alice gave the secret documents to Agent Bob.')
print(mo)

agentNamesRegex = re.compile(r'Agent (\w)\w*')
mo1 = agentNamesRegex.sub(
    r'\1****',
    'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(mo1)

# 管理复杂的正则表达式
phoneRegex = re.compile(
    r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')

phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))? # area code
(\s|-|\.)? # separator
\d{3} # first 3 digits
(\s|-|\.) # separator
\d{4} # last 4 digits
(\s*(ext|x|ext.)\s*\d{2,5})? # extension
)''', re.VERBOSE)


# 组合使用re.IGNORECASE、re.DOTALL 和re.VERBOSE
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL)
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
