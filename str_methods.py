"""
字符串的查询操作方法
"""
#1、index(), 查找子串第一次出现的位置， 若不存在则  ValueError
#2、rindex()  查找字串最后一次出现的位置，若不存在则 ValueError
s = 'hello,hello'
print(s.index('lo'))
print(s.find('lo'))
print(s.rindex('lo'))
print(s.rfind('lo'))