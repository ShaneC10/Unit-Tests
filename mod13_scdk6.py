import unittest
from datetime import datetime


# Checks that the symbol is capitalized and 1-7 letters long.
def valid_symbol(symbol):
    if symbol.isalpha() and symbol.isupper() and 1 <= len(symbol) <= 7:
        return True
    else:
        return False


# This checks that the chart type is a 1 or a 2.
def valid_chart_type(chart_type):
    if chart_type in ("1", "2"):
        return True
    else:
        return False


# This checks that the time series is a number from 1 to 4.
def valid_time_series(time_series):
    if time_series in ("1", "2", "3", "4"):
        return True
    else:
        return False


# Shows that the start date and end date are in YYYY-MM-DD format.
def valid_date(date):
    # Checks the length first so dates like 2026-1-5 do not pass.
    if len(date) != 10:
        return False

    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False


class TestInputs(unittest.TestCase):

    def test_symbol(self):
        self.assertTrue(valid_symbol("AAPL"))
        self.assertTrue(valid_symbol("IBM"))
        self.assertFalse(valid_symbol("aapl"))
        self.assertFalse(valid_symbol("ABCDEFGH"))
        self.assertFalse(valid_symbol("A1"))
        self.assertFalse(valid_symbol(""))

    def test_chart_type(self):
        self.assertTrue(valid_chart_type("1"))
        self.assertTrue(valid_chart_type("2"))
        self.assertFalse(valid_chart_type("3"))
        self.assertFalse(valid_chart_type("a"))

    def test_time_series(self):
        self.assertTrue(valid_time_series("1"))
        self.assertTrue(valid_time_series("4"))
        self.assertFalse(valid_time_series("5"))
        self.assertFalse(valid_time_series("0"))

    def test_start_date(self):
        self.assertTrue(valid_date("2026-01-15"))
        self.assertFalse(valid_date("01-15-2026"))
        self.assertFalse(valid_date("2026-02-30"))

    def test_end_date(self):
        self.assertTrue(valid_date("2026-11-20"))
        self.assertFalse(valid_date("11/20/2026"))
        self.assertFalse(valid_date("2026-13-01"))


if __name__ == "__main__":
    unittest.main()