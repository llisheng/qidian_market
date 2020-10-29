# -*- coding: utf-8 -*-
import copy

#浅拷贝
a={1:[1,2,3]}
c=a.copy()# 对a的键值对操作不会同步,但是a的子对象,就是a[0]的值 还是引用的同一个内存地址
c[2]="1"#字典c新增key为2
print(a,c)


#深拷贝
d = copy.deepcopy(a)
d[2]='1'
print(a)
print(d)
print('-----')

a[1].append(4)#通过key新增元素
print(a)
print(d)
