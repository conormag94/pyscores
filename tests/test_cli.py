import unittest


from pyscores import cli


class CLITestCase(unittest.TestCase):
    """Tests for `cli.py`."""

    def test_format_date(self):
        date_str = '2018-02-24T12:30:00Z'
        correct_date_format = 'Sat, 24 Feb 2018, 12:30'
        self.assertEqual(cli.format_date(date_str), correct_date_format)
