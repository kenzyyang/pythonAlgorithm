#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : heap.py
# @Author: yangZhenyu
# @Date  : 2018/3/1
# @Desc  :数据结构堆的python实现，仅实现其基本的操作，作为基本模块由外部算法调用

class Heap:
    def __init__(self):
        #创建一个列表代表堆,将索引为0的位置填充无意义字符
        self.pq=[0]

    def __less(self,index1,index2):
        """
        比较函数，当pq[index1]< pq[index2]时，返回True
        :param index1:
        :param index2:
        :return: boolean
        """
        if self.pq[index1]<self.pq[index2]:
            return True
        else:
            return False

    def __exch(self,index1,index2):
        """
        交换函数，将堆pq索引index1 和index2的值进行交换
        :param index1:
        :param index2:
        :return: null
        """
        #通过python的tuple操作将两个值进行交换
        self.pq[index1],self.pq[index2]=self.pq[index2],self.pq[index1]

    def __swim(self,k):
        """
        堆有序化的上浮操作，当加入一个结点大于他的父亲节点时，将该结点上浮直到满足堆关系
        :param index:
        :return: null
        """
        while k>1 and self.__less(k/2,k):
            #当未到顶层且父亲结点小于子节点时
            self.__exch(k/2,k)
            index=k/2

    def __sink(self,k):
        """
        堆有序化的下沉操作，当某个结点变得比他的子节点小时，需要通过下沉操作将小的结点沉下去
        :param k:
        :return:
        """
        N=len(self.pq)
        while(k+k<=N):
            #两倍的k 选中k 的左孩子结点
            j=k+k
            #通过比较左右孩子结点的大小，将j定位到较大的孩子上
            if j<N and self.__less(j,j+1):
                j=j+1
            #如果父亲结点的值大于孩子最大的孩子结点，则堆有序，跳出下沉操作
            if not self.__less(k,j):
                break
            #否则将父亲和孩子进行交换，然后从新的孩子结点往下找，判断是否需要进行下沉操作
            self.__exch(k,j)
            k=j

    def insert(self,dom):
        """
        向堆中插入一个新的元素，放到堆的末尾，增加堆的大小，并将堆重新调整为有序状态
        堆方法为：将其插入到堆中最末尾的地方，即使用append进行添加，然后通过上浮操作使堆重新变得有序
        :param dom:
        :return:
        """
        #第一步为将元素添加到堆的末尾
        self.pq.append(dom)
        #第二步，进行上浮操作
        self.__swim(len(self.pq))

    def delMax(self):
        """
        删除堆中最大的元素，即删除根节点，然后将末尾的结点移到根结点上，通过下沉操作将其沉到合适的位置保持堆的有序状态
        :return: 删除的最大元素 max
        """
        #将根节点与末尾的节点进行交换
        self.__exch(1,len(self.pq))
        #得到最大元素的同时将其删除
        max=self.pq.pop()
        #调用下沉操作使堆变得有序
        self.__sink(1)
        return max

    def getList(self):
        return self.pq

if __name__=="__main__":
    a=Head()
    a.insert(2)
    a.insert(6)
    a.insert(3)
    a.insert(4)
    print(a.getList())
