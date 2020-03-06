import pandas as pd
import matplotlib.pyplot as plt


yp_df = pd.read_csv('year_pop.csv')

yp_df.columns
# แสดงชื่อ columns
yp_df.info()
#non-null คือ ไม่มีข้อมูลหาย
yp_df.describe()
#ค่าเฉลี่ยเบื้องต้น


# selct year columns
year = yp_df.year
#year = yp_df(['year'],yp_df['pop']) 
pop = yp_df['pop']
#กราฟ
plt.plot(year , pop)
plt.show()

gap_df = pd.read_csv('gapminder.csv' , index_col=0)
gdp_cap = gap_df['gdp_cap']
life_exp = gap_df['life_exp']
#จุด
#แต่งรายละเอียด
plt.scatter(gdp_cap , life_exp)
plt.xscale('log')
plt.show()
