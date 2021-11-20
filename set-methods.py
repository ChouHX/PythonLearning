"""
集合的相关操作
"""
#集合的判断操作
s = {10,20,30,40,50}
print(10 in s) #True
print(100 in s) #False
print(100 not in s) #True

#集合元素的新增操作
#使用add()
s.add(80)
print(s)
#s使用update()
s.update({100,200,300}) #一次添加多个元素
print(s)
s.update(([11,21,31]))
s.update((13,1,14))
print(s)

#集合元素的删除操作
#remove()   要求元素在集合中一定存在， 否则抛出异常
s.remove(100)
print(s)
#s.remove(500) #KeyError 500

#discard()
s.discard(500) #即使元素不存在，也不会报错

#pop()  无参函数，不能自定义参数
s.pop()
#s.pop(500) #报错，不能自定义参数
print(s)

#clear()   清空集合
s.clear()
print(s)