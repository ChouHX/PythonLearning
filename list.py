
"""创建列表的的一种方式，使用[] """

lst = ['hello', 'world', 98]

"""创建列表的第二种方式，使用内置函数list()"""
lst2 = list(['heelo', 'world', 98])
print(lst)
print(lst[0])
print(lst[-3], lst2[1])


#列表的查询操作

lst3 = ['hello', 'world', 98, 'hello']
print(lst3.index('hello')) #如果列表中有相同元素只返回相同元素的第一个元素的地址
#print(lst3.index('hello', 1, 3))#ValueError: 'hello' is not in list   1，3为1 2 不包括3
print(lst3.index('hello', 1, 4))


#获取列表中的单个元素

lst4 = ['hello', 'world', 98, 'hello', 'world', 234]
#获取索引为2的元素
print(lst4[2])
#获取索引为-3的元素
print(lst4[-3])
#若列表不在指定的范围内，则报错， not in range


#获取列表中的多个元素

lst5 = [1, 2, 3, 4, 5, 6, 7]
print(lst5[1:6:2])
#lst5[1:6:2]  1为起始元素下标，6为终点元素下标，2为步长   若不声明步长，则默认为1
lst6 = lst5[1:3:1]
print(lst6)
print(lst5[1::2])  #2,4,6
print(lst5[::2])  #1,3,5,7
print('---------step步长为负数的情况-------')
print(lst5[::-1])  #第一个元素为列表最后一个元素
print('原列表', lst5)
print(lst5[6:0:-2])  #不包括下标为0的元素

#列表元素的判断及遍历

print('p' in 'python') #True
print('k' not in 'python')#True

print(10 in lst)
print(100 in lst)
print(98 in lst)
print('-----------------------')
#遍历
for item in lst:
    print(item)


#向列表的末尾添加一个元素

lstx = [10, 20, 30, 40]
print('添加之前', lstx, id(lstx))
lstx.append(100)
print('添加之后', lstx, id(lstx))
"""
append() 在列表的末尾添加一个元素
extend() 在列表的末尾至少添加一个元素
insert() 在列表的任意位置添加一个元素
"""




#列表的删除操作

"""
remove(元素值)        一次只删除一个元素，重复元素只删除第一个，元素不存在则报错  Value error
pop(元素索引)         删除指定索引位置上的元素，指定索引不存在抛出 Index error，若不指定索引则删除列表最后一个元素
clear(列表名)         清空列表
del                 删除列表 
"""

print('------------切片操作，至少删除一个元素-------------')
new_lst = lstx[0:3]
print('原列表', lstx)
print('切片后列表', new_lst)

"""
列表元素的修改操作
"""
#一次修改一个元素
print('修改前', lst)
lst[2] = 100
print('修改后', lst)

#修改列表中的多个值
lst[0:1] = [100, 200, 300]   #将0-1区间的元素修改
print('修改后', lst)


#列表元素的排序操作
#sort()方法，默认升序

lstsor = [10, 28, 13, 214, 390, 20]
print('排序前', lstsor)
lstsor.sort()
print('排序后', lstsor)
#通过关键字参数，将列表降序排序
lstsor.sort(reverse=True)
print('排序后', lstsor)

#调用内置函数，可以指定reverse = True 进行降序排序，原列表不会改变
print('------------使用内置函数进行排序，将产生一个新的列表对象-----------')
print('原列表', lstsor)
New1_lst = sorted(lstsor)
print(lstsor)
print(New1_lst)
#通过关键字参数，将列表降序排序
desc_lst = sorted(New1_lst, reverse=True)
print(desc_lst)


"""
两者区别：sort（）  原列表进行排列
sorted（）  产生一个新的列表
"""


print('------------------')
#列表生成式
lstss = [i*i for i in range(1, 10)]
print(lstss)
"""
列表中的元素的指为2，4，6，8，10
"""
lstss2 = [i*2 for i in range(1, 6)]
print(lstss2)








