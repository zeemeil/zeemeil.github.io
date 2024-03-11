# 提示
import random
num = random.randint(0,100) # 生成一个从0-100的随机整数
gamecontinue = True
while gamecontinue:
    a = int(input('请输入一个数字:'))
    print(a)
    if a == num:
        print('恭喜你猜对了，就是',a)
        break
    elif a > num:
        print('猜大了')   
    elif a < num:
        print('猜小了')