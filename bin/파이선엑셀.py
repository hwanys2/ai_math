import pandas as pd
sheet_name = {}
dfs = []
for i in range(1,9):
    dfs.append(pd.read_excel('C:/Users/User/Desktop/1학년 반배정.xlsx', sheet_name= '1-'+str(i)))
    for df in dfs:
        number = list(df['번호'])
        name = list(df['성명'])
        for j in range(1,len(df['번호'])):
            sheet_name[j] = {number[j] : name[j]}
            sheet_name.update(sheet_name[j])
ai = int(input("학반번호를 적어주세요"))
print(sheet_name[ai])

# 연습 및 시패
# import pandas as pd
# df = pd.read_excel('C:/Users/User/Desktop/명단.xls', sheet_name='sheet1')
# number = df['학번']
# name = df['이름']

# number = list(number)
# name = list(name)
# a ={}
# for i in range(40):
#     a[i]= {number[i] : name[i]}
#     a.update(a[i])
# print(a)

# print(a[10103])

# i = {}
# two = {}
# three = {}
# four = {}
# five = {}
# six = {}
# seven = {}
# eight = {}
# number = df-i['번호']
# name = df-i['성명']

# numberi=list(numberi)
# namei=list(namei)

# for j in range(26):
#     one[i]= {numberi[j] : namei[j]}
#     one.update(one[j])
# # print(one)

# df2 = pd.read_excel('C:/Users/User/Desktop/1학년 반배정.xlsx', sheet_name='1-2')
# number2 = df2['번호']
# name2 = df2['성명']
# number2 = list(number2)
# name2 = list(name2)

# for i in range(27):
#     two[i]= {number2[i] : name2[i]}
#     two.update(two[i])
# # print(two)

# df3 = pd.read_excel('C:/Users/User/Desktop/1학년 반배정.xlsx', sheet_name='1-3')
# number3 = df3['번호']
# name3 = df3['성명']
# number3 = list(number3)
# name3 = list(name3)

# for i in range(27):
#     three[i]= {number3[i] : name3[i]}
#     three.update(three[i])
# # print(three)

# df4 = pd.read_excel('C:/Users/User/Desktop/1학년 반배정.xlsx', sheet_name='1-4')
# number4 = df4['번호']
# name4 = df4['성명']
# number4 = list(number4)
# name4 = list(name4)

# for i in range(27):
#     four[i]= {number4[i] : name4[i]}
#     four.update(four[i])
# # print(four)

# df5 = pd.read_excel('C:/Users/User/Desktop/1학년 반배정.xlsx', sheet_name='1-5')
# number5 = df5['번호']
# name5 = df5['성명']
# number5 = list(number5)
# name5 = list(name5)

# for i in range(26):
#     five[i]= {number5[i] : name5[i]}
#     five.update(five[i])
# # print(three)

# df6 = pd.read_excel('C:/Users/User/Desktop/1학년 반배정.xlsx', sheet_name='1-6')
# number6 = df6['번호']
# name6 = df6['성명']
# number6 = list(number6)
# name6 = list(name6)

# for i in range(26):
#     six[i]= {number6[i] : name6[i]}
#     six.update(six[i])
# # print(three)

# df7 = pd.read_excel('C:/Users/User/Desktop/1학년 반배정.xlsx', sheet_name='1-7')
# number7 = df7['번호']
# name7 = df7['성명']
# number7 = list(number7)
# name7 = list(name7)

# for i in range(27):
#     seven[i]= {number7[i] : name7[i]}
#     seven.update(seven[i])
# # print(three)

# df8 = pd.read_excel('C:/Users/User/Desktop/1학년 반배정.xlsx', sheet_name='1-8')
# number8 = df8['번호']
# name8 = df8['성명']
# number8 = list(number8)
# name8 = list(name8)

# for i in range(26):
#     eight[i]= {number8[i] : name8[i]}
#     eight.update(eight[i])
# # print(three)


# prime = input("학반번호를 적으세요 ")
# primenumber = int(prime)
# if int(prime[1]) == 1:
#     print(one[primenumber])
# if int(prime[1]) == 2:
#     print(two[primenumber])
# if int(prime[1]) == 3:
#     print(three[primenumber])
# if int(prime[1]) == 4:
#     print(four[primenumber])
# if int(prime[1]) == 5:
#     print(five[primenumber])
# if int(prime[1]) == 6:
#     print(six[primenumber])
# if int(prime[1]) == 7:
#     print(seven[primenumber])
# if int(prime[1]) == 8:
#     print(eight[primenumber])    