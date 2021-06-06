# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 09:56:59 2021

@author: YDD
"""

import numpy as np

A = np.array([[1,0],[1,-1],[0,-1],[1,0],[1,0]])
L = np.array([[0],[0],[6],[-8],[2]])
#第一种方法
temp = np.linalg.inv(np.dot(A.T,A))
X = np.dot(temp,np.dot(A.T,L))
print(f"第一种方法的结果：\n{X}")
#第二种方法
x = np.linalg.lstsq(A,L ,rcond=None)[0]
print(f"\n第二种方法的结果：\n{x}")