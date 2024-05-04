from solution1 import Date

d1 = Date('07.12.2021')
print(d1.date)
d1.date = '14.02.2022'
print(d1.date)
print(d1.to_timestamp())
d2 = Date('32.14.2020')
print(d2.date)
d2.date = '29.02.2021'
print(d2)
d2.date = '29.02.2020'
print(d2.date)
if d1 < d2:
    print('YES')
else:
    print('NO')
print(d1 >= d2)
print(d1 != Date('01.01.2023'))
print(d1 <= d2)
