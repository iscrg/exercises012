from solution2 import Load, AirTicket

tickets = Load.write('tickets.txt')
print('-' * 79)
print('|     NAME       |FROM|TO |   DATE/TIME    |       FLIGHT       |SEAT|CLS|GATE|')
print('=' * 79)
for item in Load.data:
    print(item)
print('-' * 79)