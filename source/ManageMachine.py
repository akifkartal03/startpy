

from unittest.mock import patch
import unittest
from Automat import Automat


machine = Automat()


class AutomatMachineTestCase(unittest.TestCase):

    def test_machine_runs_correctly(self):
        user_input = ['5', '1', '1', '3', '3', '3', '3', '4', '1', '2', '7',
                      '1', '2', '3', '3', '3', '2', '4', '2', '4', '7',
                      '1', '3', '3', '3', '3', '1', '4', '5', '1', '7',
                      '1', '1', '2', '1', '3', '3', '4', '3', '2', '7',
                      '3', '1', '3', '2', '2', '3', '4', '1', '5', '7'
                      ]
        with patch('builtins.input', side_effect=user_input):
            machine.run_machine()


if __name__ == '__main__':
    unittest.main()
