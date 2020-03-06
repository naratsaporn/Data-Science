# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 18:19:10 2019

@author: MSI GP73-8RD
"""

fam = ["liz" , 1.73 , "emma" , 1.68 , "mom" , 1.71 ,"dad" , 1.89]
type(fam)


hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

areas = [hall , kit , liv , bed , bath]
print(areas)
areas

areas = ["hallway", hall, "kitchen", kit, "living room",
         liv, "bedroom", bed, "bathroom" ,bath]

#areas2 = [ ["hallway", hall]
#        , ["kitchen", kit, "living room"]
#        , [liv, "bedroom", bed, "bathroom" ,bath]]

areas
areas[0]
areas[-1]

eat_sleep_area = areas[3] + areas[7]
eat_sleep_area

downstaire = areas[0:6]
downstaire = areas[:6]

upstairs = areas[6:]
#negative index
upstairs = areas[-4:]

        #0 #1 #2
x = [["a","b","c"], #index0
     ["d","e","f"], #index1
     ["g","h","i"]] #index2
#ref row colume
#e
x[1][1]
#e f 
x[1][1:] 
x[1][1:3] #ตัวแรกเอา ตัวสองไม่เอา เช่น เอา แถว 2 ต้องเขียน 3
#b e
x[0][1]
x[1][1]

#change data in list
fam[7]
fam[7] = 1.86
 
fam[0:2]
fam[0:2] = ["lisa" , 1.74]

#adding
fam + ["me",1.68]
fam_ext = fam + ["me",1.68]
#remoning
del(fam_ext[-1])
del(fam_ext[-2:])

#07
areas[9] = 10.5
# or
areas[-1] = 10.5

areas[4] = "chill zone"

#08
areas_1 = areas + ["poolhouse", 24.5]
areas_2 = areas_1 + ["garage", 15.45]

ext_areas = areas_2[-1] + areas_2[-3]
ext_areas
# sum ไม่ได้เพราะ list มีทั้ง string และ int
# sum(areas_2)
#09
# นับมาจากข้างหน้า เริ่ม 0 ถึง ตำแหน่ง +1 ตัวข้างหลังพอดี
# นับจากข้างหลังตรงตัว
#ลบตัวหลัง 4 ค่า
del(areas_2[-4:])


del(areas_2[:2])
areas_2

areas_3 = [11.25,18.0,20.0,10.75,9.5]
#implicit copy ใช้พื้นที่ร่วมกันสองตัวแปร
areas_copy = areas_3
areas_copy[0] = 5.0
#explicit copy แยกพื้นที่ คนละตัวแปร
areas_copy = areas_3[:]
areas_copy[0] = 5.0




