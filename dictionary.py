"""
字典是Python内置的数据结构之一，与列表一样是一个可变序列
以键值对的方式存储数据，字典是一个无序的序列
"""

#字典的创建 --- 使用花括号
dic1 = {'No.': 2011,
        'Age': 21,
        'Name': "张三",
        '张三': 23
        }
print(dic1)
print(type(dic1))
#使用内置函数 ------ dict
student = dict(name='jack', age=20)
print(student)
#创建空字典
dict2 = {}
print(dict2)
#获取字典中的值  ------ 使用[]
print(dic1['Name'])
#print(dic1["dsa"]) 若查找的元素不存在，则报错KeyError
#第二种方式 -------  使用get（）方法      若查找的元素不存在，则返回None
print(dic1.get('Age'))
print(dic1.get('的撒', 99))  #99是在查找   的撒  这个值不存在时所返回的信息


"""
字典的常用操作，key的判断
"""
print('张三' in dic1)
print('张三' not in dic1)

del dic1['张三']  #删除指定的Key-value对（键值对）
#dic1.clear() #字典元素的清空操作
print(dic1)
dic1['张三'] = 98 #新增元素
print(dic1)

dic1['张三'] = 100 #修改元素的值
print(dic1)

"""
获取字典是图的三个方法
"""
#获取所有的键 keys()
keys = dic1.keys()
print(keys)
print(type(keys))

#获取所有的值 values()
values = dic1.values()
print(values)
print(type(values))

#获取所有的键值对  items()
key_values = dic1.items()
print(key_values)
print(type(key_values))
print(list(key_values))  #元组 ()  转换之后的列表元素是由元组组成的

#字典元素的遍历
for item in dic1:
        print(item, ':', dic1.get(item))


#字典生成式
#1、 内置函数 zip()
items = ['Fruit', 'Books', 'Others']
prices = [98, 78, 89, 100, 101]
lst = zip(items, prices)
print(list(lst))
d = {item.upper():price for item, price in zip(items, prices)}
print(d)