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
        """
        self.__date = self.__parse_date(date)

    @staticmethod
    def __is_leap_year(year):
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

    def to_timestamp(self):
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

    def __repr__(self):
        """
        Returns a string representation of the date.

        :return: A string representing the date.
        """
        return str(self.date)

    def __eq__(self, other):
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

    def __ne__(self, other):
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

    def __lt__(self, other):
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

    def __le__(self, other):
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

    def __gt__(self, other):
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

    def __ge__(self, other):
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
