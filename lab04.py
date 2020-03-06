
pop = [30.55 , 2.77 , 39.21]
countries = ["afghanistan" , "albania" , "algeria"]
countries.index("albania")
pop[countries.index("albania")]
# not convenient

world = {"afghanistan":30.55 , "albania" : 2.77 , "algeria" : 39.21 }
world["albania"]
# ตัวแปรมี 2 ส่วน คือ KEY , Value

world["sealand"] = 0.000027
"sealand" in world
world["sealand"] = 0.000028

del(world["sealand"])
#1 construct
europe = {'spanin' : 'madrid' , 'france':'paris', 'germany': 'berlin' , 'norway' : 'oslo' } 
#2 access
europe["spanin"]
#3
europe["italy"] = 'rome'
europe['poland'] = 'warsaw'
#4
europe["spanin"] = "barcelona"
del(europe["spanin"])

europe = {'spanin' : {'capidrid':'madrid', 'pop' : 59.83} ,
          'framce' : {'capidrid':'paris' , 'pop' : 59.83} ,
          'gramany' : {'capidrid':'berlin', 'pop' : 59.83} ,
          'norway' : {'capidrid':'oslo', 'pop' : 59.83} ,
          }
europe = ['framce']['capital']
# 
data = {'capital':'rome' , 'pop' : 59.83}
europe['italy'] = data