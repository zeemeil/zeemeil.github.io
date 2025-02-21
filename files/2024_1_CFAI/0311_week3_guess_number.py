# 提示
import random
num = random.randint(0,100) # 生成一个从0-100的随机整数
gamecontinue = True
count = 0
while gamecontinue:
    a = int(input('请输入一个数字:'))
    print(a)
    if count < 8:
        if a == num:
            print('恭喜你猜对了，就是',a)
            break
        elif a > num:
            print('第%d次猜数字，猜大了'%(count+1))
        elif a < num:
            print('第%d次猜数字，猜小了'%(count+1))
    else:
        print("已经超过5次了。")
        print("You're idolt! The turth number is %d"%num)
        break
    count += 1

