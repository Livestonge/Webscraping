import datetime


class Date:
    def __init__(self, day, month):
        self.day = day
        self.month = month


class User:

    def __init__(self, from_where, to_where, dp_date, arr_date):
        self.from_where = from_where
        self.to_where = to_where
        self.dp_date = dp_date
        self.arr_date = arr_date
        # The number of click on the calendar window to get to the arrival month.
        self.nbr_of_click_arr = abs(dp_date.month - arr_date.month)


class Month:
    """
    Each month has 4 weeks and 2 or 3 days extra. This class aim to encapsulate the specifics of each month.
     It turns out that in the calender, each month has at least 3 full weeks and often 2 non full weeks.
      Those none full weeks are the first week and last week in each month.
    """

    def __init__(self, nbr_of_days_in_the_first_week, nbr_of_days_in_the_last_week, nbr_of_extra_days):
        self.nbr_of_days_in_the_first_week = nbr_of_days_in_the_first_week
        self.nbr_of_days_in_the_last_week = nbr_of_days_in_the_last_week
        # each month has 4 weeks and few extra days.
        self.nbr_of_extra_days = nbr_of_extra_days


class MonthConstructor:

    @staticmethod
    def calculate_nbr_of_extra_days(value):

        if (((value % 2) == 0) & (value <= 6)) | (((value % 2) != 0) & (value > 6)):
            return 3
        else:
            return 2

    def construct_month(self, index):
        
        # We starts from index = 4 because we are in may in the calender for 2021.
        if index == 4:
            return Month(1, 2, 3)
        # elif index == 1:
        # return Month(0, 0, 0)
        # elif index == 2:
        # return Month(0, 3, 3)
        # elif index == 3:
        # return Month(4, 5, 2)
        elif index > 4:
            preceding_month = self.construct_month(index - 1)
            new_month = Month(0, 0, self.calculate_nbr_of_extra_days(index))
            new_month.nbr_of_days_in_the_first_week = 7 - preceding_month.nbr_of_days_in_the_last_week
            '''
            The number of days in the last week is the total of the difference between
             a full week and the number of days in the firs week of the month, and number of extra days for the month.
            '''
            nbr_of_days_in_the_last_week = (7 - new_month.nbr_of_days_in_the_first_week) + new_month.nbr_of_extra_days
            if nbr_of_days_in_the_last_week <= 7:
                new_month.nbr_of_days_in_the_last_week = nbr_of_days_in_the_last_week
            else:
                new_month.nbr_of_days_in_the_last_week = abs(7 - nbr_of_days_in_the_last_week)

            return new_month
        else:
            pass

    @staticmethod
    def construct_matrix(nbr_of_days_in_the_first_week, nbr_of_days_in_the_last_week):
        """
        This function constructs and returns the 7 days or full weeks of a month.
        :param nbr_of_days_in_the_first_week:
        :param nbr_of_days_in_the_last_week:
        :return: This function returns an array of arrays(weeks).
        """
        seven_days_weeks = []
        week = []
        max_limit = 0

        if (nbr_of_days_in_the_first_week < 3) & (nbr_of_days_in_the_last_week < 3):
            # we have 4 weeks
            max_limit = 28
        elif (nbr_of_days_in_the_first_week < 3) | (nbr_of_days_in_the_last_week < 3):
            # we have 4 weeks in this case too
            max_limit = 28
        else:
            # we have 3 weeks
            max_limit = 21

        for i in range(1, max_limit + 1):
            date = nbr_of_days_in_the_first_week + i
            week.append(date)
            if (i % 7) == 0:
                seven_days_weeks.append(week)
                week = []

        return seven_days_weeks


class Manager:

    def __init__(self, month_index):

        if (month_index < 0) | (month_index > 11):
            self.month_index = 0
        else:
            self.month_index = month_index

    def retrieve_row_and_column(self, day):

        constructor = MonthConstructor()
        month = constructor.construct_month(self.month_index)
        nbr_of_day_in_month = 0
        row = 0
        column = 0
        if month.nbr_of_extra_days == 2:
            nbr_of_day_in_month = 30
        else:
            nbr_of_day_in_month = 31

        seven_days_weeks = constructor.construct_matrix(month.nbr_of_days_in_the_first_week,
                                                        month.nbr_of_days_in_the_last_week)
        if (day <= 0) | (day > nbr_of_day_in_month):
            #  Here is day less than 0 or larger than 30 or 31.
            return row, column
        if day <= month.nbr_of_days_in_the_first_week:
            row = 0
            column = list(range(1, month.nbr_of_days_in_the_first_week)).index(day)
            return row, column
        elif day > seven_days_weeks[-1][-1]:
            if month.nbr_of_days_in_the_first_week > 0:
                row = len(seven_days_weeks) + 1
            else:
                row = len(seven_days_weeks)
            column = list(range(seven_days_weeks[-1][-1] + 1, nbr_of_day_in_month + 1)).index(day)
            return row, column
        else:
            pass

        for week in seven_days_weeks:
            for date in week:
                if date == day:
                    if month.nbr_of_days_in_the_first_week == 0:
                        row = seven_days_weeks.index(week)
                    else:
                        row = seven_days_weeks.index(week) + 1

                    column = week.index(date)
        return row, column
