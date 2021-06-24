import random
data = random.randint(0,20)
i = 0
com = 5000
while i <= 10:
    print("目前金币：", com)
    num = int(input("请输入你的数字："))
    i = i + 1
    if num < data:
        com = com - 500
        print("小了","目前金币剩余",com)
    elif num > data:
        com  = com - 500
        print("大了","目前金币剩余",com)
    else:
        com = com + 1000
        print("恭喜你，猜中了，您的猜的数字为：", num, "您猜了",i , "次了！""目前金币剩余",com)
        break
print("你的次数已用尽！Bye！！！")
