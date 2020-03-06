# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 18:50:14 2019

@author: MSI GP73-8RD
"""

var1 = [1,2,3,4]
type(var1) # ชนิด
len(var1) # จำนวนข้อมูล / ความยาว

var4 = "string"
len(var4) 
 
# help(len) 
# sorted เรียงข้อมูลจากน้อยไปมาก
# iterable คือชนิดข้อมูลที่เรียงลำดับได้
# reverse=False ถ้าไม่ใส่ค่า กำหนดให้ reverse เป็น False

first = [11.25,18.0,20.0]
second = [10.75,9.50]
#full เป็น iterable object
full = first+second
#full_sorted = sorted(full) # เรียงจากน้อยไปมาก หากไม่ใส่ argument
full_sorted = sorted(full , reverse = True) # เรียงจากมากไปน้อย descending



room = "poolhouse"
room_up = room.upper() # เปลี่ยนตัวเล็กเป็นตัวใหญ่
room.capitalize # เปลี่ยนตัวแรกเป็นตัวใหญ่
room.count("o") # หา...ว่ามีจำนวนกี่ข้อมูล

#-----------------------------------------------
# list areas มีข้อมูลของ full
# แก้ areas แล้วไม่กระทบกับ full 
areas = full[:]
areas.index(20.0)
# append เพิ่มข้อมูลต่อท้าย
areas.append(24.5)
areas.append(15.45)
areas.reverse()
areas.remove(9.5) #ลบข้อมูล...

#-----------------------------------------------
#1
import numpy
arr = numpy.array([1,2,3])
#2
import numpy as np
arr2 = np.array([1,2,3])
#3
from numpy import array
arr3 = array([1,2,3])

r = 0.43
pr = 3.14

import math
math.pi
C= 2*math.pi*r
print("Cricumfernce:" + str(C))
#หาพื้นที่
A = math.pi*(r**2)
print("Area:" + str(round(A,3)))
# round แสดงผลทศนิยม

#------------------------------------------------
r = 192500
from math import radians
dist = r*radians(12) # radians เป็น method ใน odj math
print(dist)




