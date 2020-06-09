# '''
# @Author: Jingsheng Lyu
# @Date: 2020-06-09 11:11:51
# @LastEditors: Jingsheng Lyu
# @LastEditTime: 2020-06-09 11:29:33
# @FilePath: /Python_Learning/LXF_Py/practice/quadratic.py
# '''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def quadratic(a, b, c):
    x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2 * a) 
    x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2 * a) 

    return x1, x2

print(quadratic(2, 3, 1))