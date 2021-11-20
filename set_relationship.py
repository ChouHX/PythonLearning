"""
集合之间的关系
"""
#两个集合是否相等，判断标准为：元素相同，就想等
s = {10,20,3,40,50}
s2 = {10,20,40,3,50}
print(s == s2)
print(s != s2)
""" 一个集合是否是另一个集合的子集呢"""
#集合名.issubset()
s1 = {10,20,30,40,50}
s2 = {10,20,30,40}
s3 = {10,20,90}
print(s2.issubset(s1))  #s2是s1的子集
print(s3.issubset(s1)) #s3不是s1的子集，因为90不存在


"""一个集合是否是另一个集合的超集"""
#集合名.issuperset()
print(s1.issuperset(s2))
print(s1.issuperset(s3))

"""两个集合是否没有交集"""
#集合名.isdisjoint()
print(s1.isdisjoint(s3))
s4 = {100,200,3004}
print(s1.isdisjoint(s4))



"""
集合的数学操作
"""
s1 = {10,20,40,50}
s2 = {10,20,50,49}
#交集操作
print(s1.intersection(s2))
print(s1 & s2)
#并集操作
print(s1.union(s2))
print(s1 | s2)
#差集操作
print(s1.difference(s2)) #40   相当于  A - A∩B
print(s1 - s2)
#对称差集
print(s1.symmetric_difference(s2)) #相当于 A∪B - A∩B
print(s1 ^s2)


"""
集合生成式
将{}修改为[]就是列表生成式
没有元组生成式
"""
#列表生成式
lst = [i*i for i in range(10)]
print(lst)

#集合生成式
s = {i*i for i in range(10)}
print(s)