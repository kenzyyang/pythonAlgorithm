#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 欧几里得.py
# @Author: yangZheny
# @Date  : 2018/2/7
# @Desc  :

def Euclidean(num1,num2):
    """
    欧几里得算法求两数的最大公约数
    :return:
    """
    #判断输入是否正确
    if type(num1)==type(1) and type(num2)==type(1):
        while True:
            #当num2为0时，num1为两数的最大公约数
            if num2==0:
                return num1
            else:
                #当num2不为0时，num1，num2的最大公约数等于num2 和 R 的最大公约数，其中，R为 num1和num2的余数
                num1,num2=num2,num1%num2
    else:
        print("请输入两位整数")

if __name__=="__main__":
    print("需要测试")