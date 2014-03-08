import sys
import unittest
import mock

sys.path.append('..')
from pygments_parser import *

class MergingParserTestCase(unittest.TestCase):
    def test_merge_same_tag_in_def_and_ref(self):
        mock_def_parser = mock.MagicMock()
        mock_ref_parser = mock.MagicMock()
        mock_def_parser.parse.return_value = {
            (True, 'aa', 1): 'def aa',
            (True, 'aa', 2): 'def aa'
        }
        mock_ref_parser.parse.return_value = {
            (False, 'aa', 2): '',
            (False, 'aa', 3): ''
        }
        parser = MergingParser(mock_def_parser, mock_ref_parser)
        tags = parser.parse('hello.test')
        self.assertEqual(tags, {(True, 'aa', 1):  'def aa',
                                (True, 'aa', 2):  'def aa',
                                (False, 'aa', 3): ''})

if __name__ == '__main__':
    unittest.main()
