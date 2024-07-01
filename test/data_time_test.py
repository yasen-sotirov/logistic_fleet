import unittest
from core.date_time import DateTime


class DataTime_Should(unittest.TestCase):
    def setUp(self):
        self.initial_datetime = "01/01/2023 10:00"
        DateTime.set_current_td(self.initial_datetime)

    def test_diff_between_dt(self):
        pass

    def test_add_days_to_now(self):
        pass

