import sys
import unittest

sys.path.append('..')
from pygments_parser import *

class GlobalTestCase(unittest.TestCase):
    def test_parse_langmap(self):
        langmap = parse_langmap('Ruby:.rb,C++:.cc.hh')
        self.assertEqual(langmap, {'.rb': 'Ruby',
                                   '.cc': 'C++',
                                   '.hh': 'C++'})

if __name__ == '__main__':
    unittest.main()
