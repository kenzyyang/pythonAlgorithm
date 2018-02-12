#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : sort.py
# @Author: yangZhenyu
# @Date  : 2018/2/11
# @Desc :所有排序算法的实现，不同排序算法用不同的函数封装，指定统一接受列表list型的变量，less 和 exch isSort为公用函数，sort为各个方法的不同实现

#各个使用到的python包的引用
import random
import time


#对元素进行比较，返回一个bool类型的值，将数据操作封装在该方法中可避免具体算法中具有冗长的大小比较
#该方法比较两个相同类型的数值，判断 obj1是否小于 obj2，返回bool.
def less(obj1,obj2):
    if type(obj1)==type(obj2):
        if obj1>=obj2:
            return False
        else:
            return True
    else:
        #类型不对时给出错误提示
        print("%d 和 %d 类型并不相同，无法进行比较",obj1,obj2)


#对元素进行位置交换，原理同上，避免有冗长的数据交换代码
#传入数组和两个索引，将两个索引的元素进行交换
def exch(list,index1,index2):
    #判断数据类型
    if type(list)==type([]) and type(index1)==type(1) and type(index2)==type(1):
        #判断是否数组越界
        if  index1<=len(list) and index2 <=len(list):
            #元组交换的方法，python支持这样的操作
            list[index1],list[index2]=list[index2],list[index1]
        else:
            print("索引越界,请检查算法")
    else:
        print("输入参数类型不匹配，请检查函数调用")



#测试排序算法是否成功
def isSorted():
    pass

##############################上部为公共调用的函数，下面为各个排序算法的具体实现######################################
"""
选择排序的实现
具体方法为:
扫描数组找出数组中最小的值，和数组的第一位进行交换。扫描剩下数组得到最小值，和第二位交换，依次直到最后一位。
"""
#排序算法，输入数组或者类数组的数据类型，进行排序后按照原类型进行返回，可自定义接受类型
#接受一个list数组，将其排序后返回，先按照要求写出最原始的选择排序，不考虑优化问题
#算法分析如下，在输入为n的情况下，外层循环n次，内层循环为n，n-1，n-2.......，等差数列求和得数量级为 n*(n-1)/2,时间复杂度为O(n^2),无额外的空间消耗
def selectedSort(list):
    if type(list)==type([]):
        #下面为具体的算法实现
        #外层循环做值交换操作，当内循环找到最小值后，将其赋给list[x]
        for x in range(0,len(list)):
            #记录寻找到的最小值,用当前的数进行初始化
            min=x
            #内层循环找到最小值min
            for y in range(x,len(list)):
                if less(list[y],list[min]):
                    min=y
            #循环完成之后得到最小值，将其与索引 x 进行交换
            exch(list,x,min)
        return list
    else:
        print("暂时只支持对list类型进行排序")

#测试选择排序的正确性
#测试完成
def testSelectedSort():
    list = [7, 6, 3, 7, 9, 6, 3, 1, 3, 2, 54, 1, 23, 12, 32, 63, 25]
    selectedSort(list)
    print(list)


#######################################################################################################################
"""
插入排序的实现
具体方法为:
选择数组后部分的最小值，将其插入到数组前部分的末尾
[1,2,3][5,4,7,9,8],选择4 加入到前面的位置。在同一个数组中的实现为，将4提到5的位置，其他位置依次向后移位
"""
#插入排序算法
#接受list数组，排序后返回，暂时不考虑优化
def insertSort(list):
    if type(list)==type([]):
        #下面为具体的算法实现
        #外循环记录循环已经有序的位置，同时也决定了下一个需要排序的元素
        for x in range(1,len(list)):
            #内层循环获得外循环指定的需要排序的元素，进行判断决定应该插入到前部分数组的什么位置
            #利用数组切片操作进行数组翻转得到倒序遍历的数组
            for y in range(1,x+1)[::-1]:
                #将待插入的数与已经有序的数进行比较
                #[1,2,3][a,b,c,d],当a大于3时，不操作，直接跳过。当a小于3时，a与3执行exch操作，然后继续比较，直到大于某个值为止
                if less(list[y],list[y-1]):
                    #当a小于3时，a与3进行位置交换
                    exch(list,y-1,y)
        return list
    else:
        print("暂时只支持对list类型进行排序")

#测试插入排序的正确性
#测试完成
def testSelectedSort():
    list = [4,2,5,3,1,7,6,9,8,0]
    insertSort(list)
    print(list)


#######################################################################################################################
#进行两种排序算法的比较
#其中除比较函数之外，还需要一些辅助函数去避免代码重复的问题
"""
传入任意列表list变量，通过name选择排序方法，获取执行该算法所需要的时间
"""
def calTime(list,name):
    if type(list)==type([]) and type(name)==type("abc"):
        # 开始时间
        start = time.time()
        #选择排序
        if name=="selected":
            selectedSort(list)
        #插入排序
        elif name=="insert":
            insertSort(list)
        # 结束时间
        end = time.time()
        return end - start
    else:
        print("time函数参数传递错误")

"""
随机生成乱序数组，暂定列表大小为300位，从1到100000进行取值
"""
def randomList():
    list=[]
    for x in range(0,2500):
        list.append(random.randint(1,1000000))
    return list

"""
比较排序算法性能的函数
"""
def compareSort():
    #生成乱序数组后，进行拷贝得到相同的数组避免数组在排序中被修改
    list=randomList()
    list1=list
    time1=calTime(list,"selected")
    time2=calTime(list,"insert")
    print("选择排序用时" + str(time1))
    print("插入排序用时" + str(time2))
    print("两者之比:"+str(time1/time2))

if __name__=="__main__":
    compareSort()