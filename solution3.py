class Date:
    """
    The Date class represents a date in the format "dd.mm.yyyy" and provides
    methods for parsing and comparing dates.
    """
    __MONTHS = ['янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']
    __DAY_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 10, 31, 30, 31]

    def __init__(self, date):
        """
        Initializes a Date object.

        :param date: A string representing a date in the format "dd.mm.yyyy".
        :return: None
        """
        self.__date = self.__parse_date(date)

    @property
    def date(self):
        """
        Converts the date to a timestamp.

        :return: The number of seconds since 01.01.1970.
        """
        if self.__date is not None:
            return f'{self.__date[0]} {Date.__MONTHS[self.__date[1] - 1]} {self.__date[2]} г.'
        else:
            return None

    @date.setter
    def date(self, date):
        """
        Sets the date.

        :param date: A string representing a date in the format "dd.mm.yyyy".
        :return: None
        """
        self.__date = self.__parse_date(date)

    @staticmethod
    def __is_leap_year(year) -> bool:
        """
        Checks if a year is a leap year.

        :param year: The year to check.
        :return: True if the year is a leap year, False otherwise.
        """
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    @staticmethod
    def __parse_date(date):
        """
        Parses a date from a string.

        :param date: A string representing a date in the format "dd.mm.yyyy".
        :return: A tuple containing the day, month, and year as integers.
        """
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

    def to_timestamp(self) -> int:
        """
        Converts the date to a timestamp.

        :return: The number of seconds since 01.01.1970.
        """
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

    def __repr__(self) -> str:
        """
        Returns a string representation of the date.

        :return: A string representing the date.
        """
        return str(self.date)

    def __eq__(self, other) -> bool:
        """
        Checks if this date is equal to another date.

        :param other: The other date to compare to.
        :return: True if the dates are equal, False otherwise.
        """
        day1, month1, year1 = self.__date
        day2, month2, year2 = other.__date

        if day1 == day2 and month1 == month2 and year1 == year2:
            return True
        return False

    def __ne__(self, other) -> bool:
        """
        Checks if this date is not equal to another date.

        :param other: The other date to compare to.
        :return: True if the dates are not equal, False otherwise.
        """
        day1, month1, year1 = self.__date
        day2, month2, year2 = other.__date

        if day1 != day2 or month1 != month2 or year1 != year2:
            return True
        return False

    def __lt__(self, other) -> bool:
        """
        Checks if this date is less than another date.

        :param other: The other date to compare to.
        :return: True if this date is less than the other date, False otherwise.
        """
        day1, month1, year1 = self.__date
        day2, month2, year2 = other.__date

        if day1 < day2 and month1 <= month2 and year1 <= year2:
            return True
        return False

    def __le__(self, other) -> bool:
        """
        Checks if this date is less than or equal to another date.

        :param other: The other date to compare to.
        :return: True if this date is less than or equal to the other date, False otherwise.
        """
        day1, month1, year1 = self.__date
        day2, month2, year2 = other.__date

        if day1 <= day2 and month1 <= month2 and year1 <= year2:
            return True
        return False

    def __gt__(self, other) -> bool:
        """
        Checks if this date is greater than another date.

        :param other: The other date to compare to.
        :return: True if this date is greater than the other date, False otherwise.
        """
        day1, month1, year1 = self.__date
        day2, month2, year2 = other.__date

        if day1 > day2 and month1 >= month2 and year1 >= year2:
            return True
        return False

    def __ge__(self, other) -> bool:
        """
        Checks if this date is greater than or equal to another date.

        :param other: The other date to compare to.
        :return: True if this date is greater than or equal to the other date, False otherwise.
        """
        day1, month1, year1 = self.__date
        day2, month2, year2 = other.__date

        if day1 >= day2 and month1 >= month2 and year1 >= year2:
            return True
        return False


class Load:
    """
    The Load class provides a static method for loading air ticket data from a file.
    """
    data = []

    @staticmethod
    def write(
            meeting_file_name: str,
            persons_file_name: str,
            pers_meetings_file_name: str
    ):
        """
        Loads meeting and user data from the specified files.

        :param meeting_file_name: The name of the file containing meeting data.
        :param persons_file_name: The name of the file containing user data.
        :param pers_meetings_file_name: The name of the file containing meeting-user associations.
        """
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
    """
    The User class represents a user with various personal attributes.
    """
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
        """
        Initializes a User object.

        :param id: The user's ID.
        :param nick_name: The user's nickname.
        :param first_name: The user's first name.
        :param last_name: The user's last name.
        :param middle_name: The user's middle name.
        :param gender: The user's gender.
        """
        self.id = id
        self.nick_name = nick_name
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.gender = gender


class Meeting:
    """
    The Meeting class represents a meeting with various attributes including ID, date, title, and employees.
    """
    lst_meeting = []

    def __init__(
            self,
            id: int,
            date: Date,
            title: str,
    ):
        """
        Initializes a Meeting object.

        :param id: The meeting's ID.
        :param date: The date of the meeting.
        :param title: The title of the meeting.
        :return: None
        """
        self.id = int(id)
        self.date = date
        self.title = title
        self.employees = []

    def add_person(self, person):
        """
        Adds a person to the meeting.

        :param person: The person to add.
        :return: None
        """
        self.employees.append(person)

    def count(self):
        """
        :return: None
        """
        pass

    @staticmethod
    def count_meeting(date: Date) -> int:
        """

        :param date:
        :return: None
        """
        counter = 0
        for meet in Meeting.lst_meeting:
            if meet.date == date:
                counter += 1
        return counter

    @staticmethod
    def total() -> int:
        """
        Counts the total number of people in all meetings.

        :return: The total number of people in all meetings.
        """
        counter = 0
        for meet in Meeting.lst_meeting:
            counter += len(meet.employees)
        return counter

    def __repr__(self) -> str:
        """
        Returns a string representation of the meeting.

        :return: A string representing the meeting.
        """
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
