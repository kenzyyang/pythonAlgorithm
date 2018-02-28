#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : queue.py
# @Author: yangZhenyu
# @Date  : 2018/2/27
# @Desc  :优先队列的具体实现

import random
import sort

"""
优先队列：
该数据结构支持两种操作：1.删除最大元素。 2.插入元素。
该类作为所有队列的父类，定义基本的接口并且实现，子类继承后根据不同队列的特殊需求进行函数覆盖
"""
class queue:
    def __init__(self,outList=[]):
        #构造方法，创建一个队列")
        if type(outList)==type([]):
            self.list=outList
        else:
            print("创建queue时，参数传递错误")

    def size(self):
        """
        获得队列大小
        :return: size
        """
        return len(self.list)

    def max(self):
        """
        返回最大元素
        :return: maxDom
        """
        # 通过遍历数组一一对比，得到最大的元素
        if self.isEmpty():
            print("")
        max=self.list[0]
        for x in range(1,len(self.list)):
            if sort.less(max,self.list[x]):
                max=self.list[x]
        return max


    def insert(self,dom):
        """
        接受一个可比较的类型，将其插入到队列中,具体实现在有序和无序队列中并不相同
        :param dom:
        :return:
        """
        #python中数组并没有大小限制，顾不做队列填充满的判断，直接进行插入
        self.list.append(dom)

    def delMax(self):
        """
        删除队列中最大的那个元素，将其值或者索引返回
        :return:
        """
        self.list.remove(self.max())


    def isEmpty(self):
        """
        bool类型，返回队列是否为空
        :return: true or false
        """
        if len(self.list)==0:
            return True
        else:
            return False

"""
数组实现的有序队列：
特点是，在插入操作时，通过特定的排序算法将其队列本身变得有序，这样在删除最大元素时可以直接删除最右边的元素，即和栈的pop操作相同
我的做法是：在创建队列时，若是通过list参数进行创建，则先进行一次排序，可选择任意排序方法，但考虑到规模较大，暂时使用快速排序
"""
class orderedArrayQueue(queue):

    def __init__(self,outList=[]):
        """
        先通过快速排序将列表有序化，然后将列表传给父级的构造函数创建对应的私有变量
        :param outList:
        """
        quick=sort.Quick()
        quick.quickSort(outList)
        queue.__init__(outList)

    def insert(self,dom):
        """
        有序队列，选择特定的插入位置确定整个队列是有序的
        :param dom:
        :return:
        """


