import pandas as pd
df = pd.read_excel (r'C:\Users\USER\Downloads\covid_19_data.xlsx')
df1 = pd.read_excel (r'C:\Users\USER\Downloads\FINAL TABLE.xlsx') # seed data and merketline data already combined
final1=pd.merge(df1,df,on='City',how='outer')
df2 = pd.read_excel (r'C:\Users\USER\Downloads\world-cities_geonsmeid.xlsx')
final2=pd.merge(final1,df2,on='City',how='outer')
df3 = pd.read_excel (r'C:\Users\USER\Downloads\11_2_1_Percentage_Access_to_Public_Transport.xlsx')
final3=pd.merge(final2,df3,on='City',how='outer')
df4 = pd.read_excel (r'C:\Users\USER\Downloads\Cities by Sunshine Duration.xlsx')
final4 = pd.merge(final3,df4,on='City',how='outer')
final4.to_excel("output.xlsx")