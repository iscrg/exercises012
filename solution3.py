class Date:
    __MONTHS = ['янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']
    __DAY_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 10, 31, 30, 31]

    def __init__(self, date):
        self.__date = self.__parse_date(date)

    @property
    def date(self):
        if self.__date is not None:
            return f'{self.__date[0]} {Date.__MONTHS[self.__date[1] - 1]} {self.__date[2]} г.'
        else:
            return None

    @date.setter
    def date(self, date):
        self.__date = self.__parse_date(date)

    @staticmethod
    def __is_leap_year(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    @staticmethod
    def __parse_date(date):
        parts = date.split('.')

        if len(parts) != 3:
            print('ошибка')
            return None

        day, month, year = map(int, parts)

        if not (1 <= month <= 12 and year > 1970):
            print('ошибка')
            return None

        if month == 2 and Date.__is_leap_year(year):
            day_in_month = Date.__DAY_IN_MONTH[month - 1] + 1
        else:
            day_in_month = Date.__DAY_IN_MONTH[month - 1]

        if not day <= day_in_month:
            print('ошибка')
            return None

        return day, month, year

    def to_timestamp(self):
        result = 0
        day, month, year = self.__date

        if self.__date is None:
            raise Exception("No date has been set.")

        for y in range(1970, year):
            if Date.__is_leap_year(y):
                result += 366 * 24 * 60 * 60
            else:
                result += 365 * 24 * 60 * 60

        for m in range(1, month):
            result += Date.__DAY_IN_MONTH[m - 1] * 24 * 60
            if m == 2 and Date.__is_leap_year(month):
                result += 24 * 60

        result += day * 24 * 60

        return result

    def __repr__(self):
        return str(self.date)

    def __eq__(self, other):
        day1, month1, year1 = self.__date
        day2, month2, year2 = other.__date

        if day1 == day2 and month1 == month2 and year1 == year2:
            return True
        return False

    def __ne__(self, other):
        day1, month1, year1 = self.__date
        day2, month2, year2 = other.__date

        if day1 != day2 or month1 != month2 or year1 != year2:
            return True
        return False

    def __lt__(self, other):
        day1, month1, year1 = self.__date
        day2, month2, year2 = other.__date

        if day1 < day2 and month1 <= month2 and year1 <= year2:
            return True
        return False

    def __le__(self, other):
        day1, month1, year1 = self.__date
        day2, month2, year2 = other.__date

        if day1 <= day2 and month1 <= month2 and year1 <= year2:
            return True
        return False

    def __gt__(self, other):
        day1, month1, year1 = self.__date
        day2, month2, year2 = other.__date

        if day1 > day2 and month1 >= month2 and year1 >= year2:
            return True
        return False

    def __ge__(self, other):
        day1, month1, year1 = self.__date
        day2, month2, year2 = other.__date

        if day1 >= day2 and month1 >= month2 and year1 >= year2:
            return True
        return False


class Load:
    data = []

    @staticmethod
    def write(
            meeting_file_name: str,
            persons_file_name: str,
            pers_meetings_file_name: str
    ):
        with open(meeting_file_name, 'r', encoding='UTF-8') as f:
            for line in [line.rstrip() for line in f.readlines()][1:]:
                id, date, title = line.split(';')[:-1]
                Meeting.lst_meeting.append(Meeting(int(id), Date(date), title))

        with open(persons_file_name, 'r', encoding='UTF-8') as f:
            for line in [line.rstrip() for line in f.readlines()][1:]:
                id, nick_name, first_name, last_name, middle_name, gender = line.split(';')[:-1]
                User.users.append(User(int(id), nick_name, first_name, last_name, middle_name, gender))

        with open(pers_meetings_file_name, 'r', encoding='UTF-8') as f:
            for line in [line.rstrip() for line in f.readlines()][1:]:
                id_meet, id_pers = line.split(';')[:-1]
                for meet in Meeting.lst_meeting:
                    if meet.id == int(id_meet):
                        for user in User.users:
                            if user.id == int(id_pers):
                                meet.employees.append(user)


class User:
    users = []

    def __init__(
            self,
            id: int,
            nick_name: str,
            first_name: str,
            last_name: str,
            middle_name: str,
            gender: str,
    ):
        self.id = id
        self.nick_name = nick_name
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.gender = gender


class Meeting:
    lst_meeting = []

    def __init__(
            self,
            id: int,
            date: Date,
            title: str,
    ):
        self.id = int(id)
        self.date = date
        self.title = title
        self.employees = []

    def add_person(self, person):
        self.employees.append(person)

    def count(self):
        pass

    @staticmethod
    def count_meeting(date: Date):
        counter = 0
        for meet in Meeting.lst_meeting:
            if meet.date == date:
                counter += 1
        return counter

    @staticmethod
    def total():
        counter = 0
        for meet in Meeting.lst_meeting:
            counter += len(meet.employees)
        return counter

    def __repr__(self):
        res = ''

        res += f'Рабочая встреча {Meeting.lst_meeting.index(self) + 1}\n'
        res += f'{self.date} {self.title}\n'

        for employee in self.employees:
            employee_str = (f'ID: {employee.id} '
                            f'LOGIN: {employee.nick_name} '
                            f'NAME: {employee.first_name} {employee.middle_name} {employee.last_name} '
                            f'GENDER: {employee.gender}')
            employee_str = ' '.join(employee_str.split())
            employee_str += '\n'
            res += employee_str
        return res
