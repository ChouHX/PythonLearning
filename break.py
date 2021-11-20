import random
x = random.randint(1, 9)
print(x)
s = 0
#break案例：猜数字游戏
while 1:
    print('guess what is it?input your number:')
    n = int(input())
    if n == x:
        print('cool!you are right!')
        break
    elif n > x:
        print('Nope!The number is too big!input again')
        s += 1
    elif n < x:
        print('Nope!The number is too small!input again')
        s += 1
    if s == 5:
        print('you have run out of opportunities')
        break

print('Program is power off!')