#
# Copyright (c) 2014
#	Yoshitaro Makise
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

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
