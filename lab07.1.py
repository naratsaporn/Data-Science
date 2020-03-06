import pandas as pd
import matplotlib.pyplot as plt

yp_df=pd.read_csv("D:/2562/Data Science (DTI 511)/gapminder_04.csv")

#อยากรู้ชื่อ column ว่ามีอะไรบ้าง ใช้คำสั่งอย่างไร
yp_df.columns
yp_df.info()
yp_df.describe()

#select column year
year=yp_df.year
#select column pop only
pop=yp_df['pop']

#plt.plot(yp_df['year'],yp_df['pop'])
plt.plot(year,pop)
#plt.show()

gap_df = pd.read_csv("D:/2562/Data Science (DTI 511)/gapminder_04.csv", index_col=0)
gdp_cap = gap_df['gdp_cap']
life_exp = gap_df['life_exp']

le = life_exp[21:70]
gc = gdp_cap[21:70]

#plt.plot(gdp_cap, life_exp)
#plt.scatter(gdp_cap, life_exp)
plt.scatter(gdp_cap, life_exp, s=gap_df['population']/1000000, c=gap_df['color'], alpha=0.8)
plt.xscale('log')
xlabel="GDP per Capital [in USD]"
plt.xlabel(xlabel)
ylabel="Life Expectancy [in Years]"
plt.ylabel(ylabel)
title="World Development in 2007"
plt.title(title)

#แกน x เป็นตัวเลข 10 ยกกำลัง 3 อาจจะดูยาก
tick_val=[1000,10000,100000]
tick_lab=['1K','10K','100K']
plt.xticks(tick_val,tick_lab)

plt.text(1550, 71, 'India')

plt.text(5700, 80, 'a')

plt.grid(True)

plt.show()


"""
year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]
plt.plot(year, pop)
plt.show()