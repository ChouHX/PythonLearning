#嵌套循环

for i in range(4):
    for x in range(3):
        print('Python', end='\t')
    print()


x = 1
while x <=3:
    for y in range(1,4):
        print(x, ',', y, end='\t')
    print()
    x+= 1

#嵌套循环案例：九九乘法表
for i in range(1,10):
    for s in range(1,i+ 1):
        print(s, '*', i ,'=', i* s , end='\t')
    print()

#二重循环中的break 和 continue

for i in range(1, 6):
    for x in range(1, 11):
        if x % 2 == 0:
            continue
        print(x, end='\t')
    print()
else:
    print('down')

for i in range(1, 6):
    for x in range(1, 11):
        if x % 2 == 0:
            break
        print(x, end='\t')
    print()
else:
    print('down')