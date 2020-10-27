# -*- coding: utf-8 -*-
# author:lisheng
#1计算机出一个1~100之间的随机数，人输入自己猜的数字，计算机给出对应的提示信息，直到人猜出计算机出的数字
import random
answer=random.randint(1,100)
count=1
while True:
    count+=1
    nub=int(input("请输入数字"))
    if nub < answer:
        print ("再大一点")
    elif nub > answer:
        print ("小一点")
    else:
        print ("猜对了")
        break
    print ("你总共猜了%s次  % (count)")

#2.使用while 循环,打印出 1到100之间 能被3 和 5 整除的数字
count=1
while count <100:
    count+=1
    if count %3==0 and count % 5==0:
        print (count)

#3. 使用while 循环,打印出 1到100之间 能被3 和 5 整除的数字,打印4个数字后就停止循环
a=1
i = 0
while a <100 and i < 4:
    a+=1
    if a %3==0 and a % 5==0:
        i+=1
        print (a)


