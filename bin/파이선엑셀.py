import pandas as pd
df = pd.read_excel('C:/Users/User/Desktop/명단.xls', sheet_name='sheet1')
number = df['학번']
name = df['이름']

number = list(number)
name = list(name)
good = []
for i in range(40):
    good.append({number[i] : name[i]})
print(good)

print(good[5])