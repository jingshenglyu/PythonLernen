#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# '''
# @Author: Jingsheng Lyu
# @Date: 2020-06-10 08:15:03
# @LastEditors: Jingsheng Lyu
# @LastEditTime: 2020-06-10 08:18:37
# @FilePath: /C_Learning/home/jingsheng/Python_Learning/LXF_Py/practice/3.4. Hanoi.py
# '''

def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

move(4, 'A', 'B', 'C')