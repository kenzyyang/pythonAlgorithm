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
    """
    obj1 >= obj2 return Flase
    else return True
    :param obj1:
    :param obj2:
    :return:
    """
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
            y=x
            while y>=1:
                # 将待插入的数与已经有序的数进行比较
                # [1,2,3][a,b,c,d],当a大于3时，不操作，直接跳过。当a小于3时，a与3执行exch操作，然后继续比较，直到大于某个值为止
                if less(list[y], list[y - 1]):
                    # 当a小于3时，a与3进行位置交换
                    exch(list, y - 1, y)
                y=y-1
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
"""
希尔排序的实现
具体思想为：
选择一个递增的数组，例如h=3h+1，最开始将得到一个最接近与数组长度的h，将数组分为h个组，每个组之间的元素间隔为h
这样可满足数组元素之间跨h距离的交换，解决插入排序元素之间两两交换性能较差的问题
之后不断将h进行缩小得到更少的数组，但在之后进行排序时，数组已经部分有序，元素之间只需要少量的移动就可以到达最终的位置
最后，h=1时，即是对原数组进行插入排序
"""
def shellSort(list):
    if type(list)==type([]):
        N=len(list)
        #按照书的要求暂时让h=3，h=3*h+1
        h = 1
        while h<(N/3):
            h=3*h+1
        #将数组变为分成h个序列，通过插入排序让这h个序列变得有序，最外层循环进行组的选择，将h不断的缩小，
        while h>=1:
            for x in range(h,N):
                #将list[x] 插入到list[x-h] list[x-2h]....中
                y=x
                while y>=h:
                    if less(list[y],list[y-h]):
                        exch(list,y,y-h)
                    else:
                        break
                    y=y-h
            h=h/3
        return list
    else:
        print("暂时只支持list类型排序")

def testShell():
    list=[4,2,3,6,9,7,8,0,1,5]
    shellSort(list)
    print list

#######################################################################################################################
"""
自顶向下归并排序的实现
具体思想为：
自顶向下的归并法思想为，将数组分为两个更小的数组，将两个更小的数组变为有序，然后将这两个有序的数组归并为一个有序的数组。
不断递归下去时可以得到，最后数组将细分为两个元素之间的有序处理。
"""
class Merge:
    def __init__(self):
        #归并排序所需要的辅助空间
        self.aux=list()

    def mergeSort(self,list):
        if type(list)==type([]):
            #进行aux辅助数组的初始化
            for x in range(0,len(list)):
                self.aux.append(x)
            self.__sort(list,0,len(list)-1)
        else:
            print("不支持非list参数排序")

    def __sort(self,list,index1,index2):
        """
        将list数组从index1 到index2 变为有序，向下递归
        :param list:
        :param index1:
        :param index2:
        :return:
        """
        #当执行到该步骤时说明已经排序好，不用向下再递归
        if index1>=index2:
            return
        mid=index1+(index2-index1)/2
        self.__sort(list,index1,mid)
        self.__sort(list,mid+1,index2)
        self.__merge(list,index1,mid,index2)
    def __merge(self,list,index1,mid,index2):
        """
        将两个已经有序的子数组进行归并，变为一个有序的大数组
        :param list:
        :param index1:
        :param mid:
        :param index2:
        :return:
        """
        i=index1
        j=mid+1
        #将数组复制到aux辅助数组中
        for x in range(index1,index2+1):
            self.aux[x]=list[x]
        #将aux进行归并合为一个大有序数组赋值回原数组
        for x in range(index1,index2+1):
            if i > mid:
                #第一个数组已经归并完成，将第二个数组依次归并回原数组
                list[x]=self.aux[j]
                j=j+1
            elif j > index2:
                #同上，第二个数组归并完成，将第一个数组归并回原数组
                list[x]=self.aux[i]
                i=i+1
            elif less(self.aux[j], self.aux[i]):
                #两个数组的值进行比较，选择较小的一个，j 值小则归并j
                list[x]=self.aux[j]
                j=j+1
            else:
                #i 值小则归并 i
                list[x]=self.aux[i]
                i=i+1
    def testSort(self):
        a=[6,2,5,4,1,3,8,9,7,0]
        self.mergeSort(a)
        print a


"""
自底向上归并排序的实现
具体思想为：
我们将一个较大的数组最开始就细分为一个一个的元素，默认一个元素为一个小数组，将其两两归并，得到一些数组，这些数组有两个元素且有序
将其继续归并，得到有四个元素的数组，一直向上直到归并为最大的数组
"""
#继承自Merge类，对方法进行一定的修改
class MergeUp(Merge):
    def __mergeSort(self,list):
        if type(list)==type([]):
            N=len(list)
            #给aux数组进行初始化赋值
            for x in range(0,N):
                self.aux.append(x)
            #子数组的大小
            size=1
            while size<N:
                subIndex=0
                while subIndex<N-size:
                    self.__merge(list,subIndex,subIndex+size-1,min(subIndex+size+size-1,N-1))
                    subIndex+=size+size
                size=size+size
        else:
            print("暂时只支持list类型")


"""
快速排序的实现：
思想：与归并排序对应，也是分治法的典型例子。归并排序是将数组分为两个子数组，将子数组排序之后进一步排序合为一个有序的大数组
而快速排序在分隔数组时是有选择的，以某个元素 K 为分隔线，第一个数组都小于K，第二个数组元素都大于K，这样，当两个子数组有序时，原数组自然有序
个人理解就是，归并排序在list[mid]<=list[mid+1]时的特殊例子，但递归调用的时间并不一样
"""
class Quick:
    def quickSort(self,list):
        if type(list)==type([]):
            #随机打乱数组避免快排进入到效率最低的状态
            random.shuffle(list)
            self.__sort(list,0,len(list)-1)
        else:
            print("只支持list类型的排序")
    def __sort(self,list,index1,index2):
        """
        递归函数
        :param list:
        :param index1:
        :param index2:
        :return:
        """
        if (index1+10) >=index2:
            #算法改进策略，当细分到比较小的数组时，对于小数组用插入排序速度会更快
            #暂时定为在数组大小为10左右时进行插入排序
            insertSort(list[index1:index2])
            return
        j=self.__partition(list,index1,index2)
        self.__sort(list, index1, j - 1)
        self.__sort(list, j+1, index2)

    def threeWay(self,list):
        """
        三向快速排序方法，将数组切分为三个数组，第一个的所有元素切分元素小，第二个的所有元素等于切分元素，第三个的所有元素大于切分元素
        这种方法在数组中有大量重复的数据时性能明显好于普通的快速排序
        :param list:
        :return:
        """
        self.__threeWaySort(list,0,len(list)-1)

    def __threeWaySort(self,list,index1,index2):
        if index2<=index1:
            return
        lt=index1
        i=index1+1
        gt=index2
        partDom=list[index1]
        while i<=gt:
            cmp=compare(list[i],partDom)
            if cmp<0:
                exch(list,lt,i)
                lt+=1
                i+=1
            elif cmp>0:
                exch(list,i,gt)
                gt-=1
            else:
                i+=1
        self.__threeWaySort(list,index1,lt-1)
        self.__threeWaySort(list,gt+1,index2)


    def __partition(self,list,index1,index2):
        """
        切分数组的子函数,将数组切分为三个部分,数组1，切分元素，数组2，每次切分将会找到切分元素对应的最终位置
        方法为：从左向右扫描指针，当左边遇到比切分元素小，右边遇到比切分元素大的元素时，将两者进行交换。
        当指针接触时，将比切分元素小的最右边的元素和切分元素进行交换，即确定了切分元素的位置
        :param list:传入的数组
        :param index1:开始索引
        :param index2:结束索引
        :return:切分元素对应的索引j
        """
        #这个判断目的是在进行单个元素为一个数组的快排切片时直接返回某个值，避免进入死循环
        left=index1
        right=index2+1
        #指定每次的最左边元素为切分元素
        partDom=list[left]
        while True:
            while True:
                left=left+1
                if less(partDom,list[left]) or left==index2:
                    #如果找到一个比切分元素大的元素，跳出这层循环
                    break
            while True:
                right=right-1
                if less(list[right],partDom) or right==index1:
                    #同上
                    break
            if left>=right:
                #当left大于right时，正好是左边进入右边数组，右边进入左边数组的时候，将小于切分元素的最右边的值，即right索引所对应的位置与切分元素进行交换即可
                break
            #将比 分隔元素小但在右边和比分隔元素大但在左边的元素进行交换
            exch(list,left,right)

        exch(list,index1,right)
        return right


    def testQuick(self):
        a=randomList()
        b=MergeUp()
        b.mergeSort(a)
        print a
        self.quickSort(a)
        print a

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
        elif name=="shell":
            shellSort(list)
        elif name=="merge":
            merge=Merge()
            merge.mergeSort(list)
        elif name=="mergeup":
            mergeup=MergeUp()
            mergeup.mergeSort(list)
        elif name=="quick":
            quick=Quick()
            quick.quickSort(list)
        elif name=="3wayquick":
            quick = Quick()
            quick.threeWay(list)
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
    for x in range(0,700):
        list.append(random.randint(0,100000))
    return list

"""
compare接口，接受两个可比较的对象，返回两者之间的差
"""
def compare(obj1,obj2):
    if type(obj1)==type(obj2):
        return obj1-obj2
    else:
        print("compare函数接受了两个不可比较的参数")

"""
比较排序算法性能的函数
"""
def compareSort():
    #生成乱序数组后，进行拷贝得到相同的数组避免数组在排序中被修改
    list=randomList()
    list1=list[::]
    time1=calTime(list,"3wayquick")
    time2=calTime(list1,"quick")
    print("3wayquick排序和quick排序用时比为"+str(time1/time2))

if __name__=="__main__":
    compareSort()