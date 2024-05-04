from solution3 import Load, Meeting, User, Date

Load.write('meetings.txt', 'persons.txt', 'pers_meetings.txt')
for item in Meeting.lst_meeting:
    print(item)
print(Meeting.total())
print(Meeting.count_meeting(Date('21.04.2020')))
