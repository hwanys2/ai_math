import pandas as pd
df = pd.read_excel('C:/Users/User/Desktop/명단.xls', sheet_name='sheet1')
number = df['학번']
name = df['이름']

number = list(number)
name = list(name)
a ={}
for i in range(40):
    a[i]= {number[i] : name[i]}
    a.update(a[i])
print(a)

print(a[10103])
