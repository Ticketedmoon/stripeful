import unittest
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

class TestTimeBehaviour(unittest.TestCase):

    def test_1_date_time_today(self):
        # These are the same
        print(datetime.today())
        print(datetime.now())
        # Extract only date component
        print(datetime.now().date())
        # Extract only time component
        print(datetime.now().time())

    def test_2_date_time_conversion(self):
        date_string = "Feb 25 2020 4:20PM"
        parsed_date_time_object = datetime.strptime(date_string, '%b %d %Y  %I:%M%p')
        print(parsed_date_time_object)

        date_string = "21/11/06 16:30"
        dt = datetime.strptime(date_string, "%d/%m/%y %H:%M")
        print(dt)

    def test_3_date_minus_7_days(self):
        given_date = datetime(2020, 2, 25)
        new_date = given_date - timedelta(days=7)
        print("given={0}, new={1}".format(given_date, new_date))

    def test_4_print_date_in_format(self):
        given_date = datetime(2020, 2, 25)
        # expected Tuesday 25 February 2020
        formatted_dt = given_date.strftime("%A %d %B %Y")
        print(formatted_dt)

    def test_5_find_day_of_week_given_date(self):
        given_date = datetime(2020, 7, 26)
        formatted_dt = given_date.strftime("%A")
        print("Integer Day-of-Week value (0-6): {0}, Day-of-Week text value: {1}".format(given_date.weekday(), formatted_dt))

    def test_6_add_7_days_and_12_hours_to_date(self):
        given_date = datetime(2020, 3, 22, 10, 0, 0)
        new_date = given_date + timedelta(days=7, hours=12)
        print("given={0}, new={1}".format(given_date, new_date))

    def test_7_print_current_time_in_ms(self):
        dt = datetime.now().timestamp()
        ms_now = dt * 1000
        print(ms_now)

    def test_8_convert_datetime_to_str(self):
        given_date = datetime(2020, 2, 25)
        string_date = given_date.strftime("%Y-%m-%d %H:%M:%S")
        # "2020-02-25 00:00:00"
        print(string_date)

    def test_9_calculate_date_plus_4_hours(self):
        given_date = datetime(2020, 2, 25).date()
        new_date = given_date + relativedelta(months=4)
        print("given: {0}, new: {1}".format(given_date, new_date))

    def test_a10_calculate_number_days_between_2_days(self):
        # 2020-02-25
        date_1 = datetime(2020, 2, 25)
        # 2020-09-17
        date_2 = datetime(2020, 9, 17)
        diff = date_2 - date_1
        print("diff days: {0}".format(diff.days))

if __name__ == '__main__':
    unittest.main()
