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
