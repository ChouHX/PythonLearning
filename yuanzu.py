"""
元组
"""
#可变序列  ：  列表  字典   可以进行增删改的操作
lst = [10,20,30]
print(id(lst))
lst.append(300)
print(id(lst))#元素增加或更改后，地址不变，为可变序列
#不可变序列，没有增删改的操作
s = 'hello'
print(id(s))
s = s + 'world'
print(id(s))#发生更改后地址随之更换

#元组的创建方式
#第一种： 使用小括号 ()
t = ('Python', 'World', 98)
print(t)
print(type(t))
t2 = 'Python', 'world', 98 #省略了小括号
#如果元组中只包含一个元素，则需要使用逗号和小括号
t3 = ('X',)
print(type(t3))
print(type(t2))
#第二种创建方式，使用内置函数 tuple()
t1 = tuple(('Python', 'C'))
print(t1)
print(type(t1))

#空元组的创建
lst = []
lst1 = list()

d = {}
d1 = dict()

#空元组
t4 = ()
t5 = tuple()

print('空列表', lst, lst1)
print('空字典', d, d1)
print('空元组', t4, t5)

tx = (10, [20, 30], 9)
print(tx)
print(type(tx))
print(tx[0], type(tx[0]), id(tx[0]))
print(tx[1], type(tx[1]), id(tx[1]))
print(tx[2], type(tx[2]), id(tx[2]))
"""尝试将t[1]修改为100"""
print(id(100))
#tx[1] = 100 #error
#由于[10,20]是列表，而列表是可变序列，所以可以向列表中添加元素，而列表的内存地址不变
tx[1].append(100)
print(tx)


"""
元组的遍历，元组是可迭代对象，所以可以使用 for...in进行遍历
"""
t01 = ('Python', 'world', 98)
#第一种获取猿族元素的方式，使用索引
print(t01[0])
print(t01[1])
#第二种方式： 遍历元组
for item in t01:
    print(item, end='\t')