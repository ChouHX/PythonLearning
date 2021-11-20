"""
集合是没有value的字典
与列表、字典一样，都属于可变类型的序列
"""
#集合的创建
#1、使用花括号 {}
s = {2,3,4,5,5,6,7,7,}
print(s) #集合中的元素不允许重复，会把重复的去掉

#2、使用内置函数 set()
s1 = set(range(6)) #将0-5的整数序列通过内置函数set整合为集合
print(s1, type(s1))
s2 = set([1,2,3,4,4,5,5,6]) #将列表装换为集合
s2 = set((1,2,3,4,5,6)) #将元组转换为集合    集合中的元素是无序的
s4 = set('Python')
print(s4,type(s4))
s5 = set({1,2,3,4,5})
print(s5, type(s5))

#定义一个空集合
s6 = {}
print(type(s6)) #显示为字典类型
s7 = set()
print(type(s7))