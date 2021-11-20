"""
else的三种用法
if else
while else
for  else
"""

for i in range(3):
    pwd = input('input your password:')
    if pwd == '888':
        print('Yes')
        break
    else:
        print('No,input again')
else:
    print("You have run out of your opportunity!")

x = 0
while x < 3:
    n = input('please input your password:')
    if n == '888':
        print('Yes')
        break
    else:
        print('No')
        x += 1
else:
    print("You have run out of your opportunity!")