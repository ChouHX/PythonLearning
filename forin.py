for item in 'Python':
    print(item)

for i in range(10):
    print(i)

#for in 案例：水仙花数
for x in range(100, 1000):
    ge = x % 10
    #Python 不同于 C语言，//为除以
    shi = x // 10 % 10
    bai = x // 100
    if ge**3 + shi**3 + bai**3 == x:
        print(x)