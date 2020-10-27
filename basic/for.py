# # -*- coding: utf-8 -*-
alist = ['哈', '楼', 4, 5, 1, 2, 3]
blist = ['哈', '楼', 'wo', 'de', 1, 2, 3]
# 请使用for循环遍历列表的方式 求出两个列表的 交集(两个列表都包含的元素)和差集(alist中有的元素blist中没有和blist中有的元素alist中没有的元素)
jiao=[]
cha=[]
for i in blist:
    if i in alist:
        jiao.append(i)
    else:
        cha.append(i)
print(jiao)
print(cha)
#新增的一行注释