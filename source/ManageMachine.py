

from unittest.mock import patch
import unittest
from Automat import Automat


machine = Automat()
class ContainersTestCase(unittest.TestCase):

    def test_get_input_stacks_processed_input_correctly(self):
        user_input = [
            '1',
            '1',
            '1',
            '3',
            '3',
            '3',
            '3',
            '4',
            '1',
            '2',
            '7',
        ]
        expected_cash = {'25Kurus': 19, '50Kurus': 19, '1TL': 9}
        with patch('builtins.input', side_effect=user_input):
            machine.run_machine()
        self.assertEqual(machine.cash_box, expected_cash)


if __name__ == '__main__':
    unittest.main()
