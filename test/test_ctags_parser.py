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

class CtagsParserTestCase(unittest.TestCase):
    def test_parse_multiple_paths(self):
        options = ParserOptions()
        parser = CtagsParser('./ctags_stub.py', options)
        tags = parser.parse('hello.test')
        self.assertEqual(tags, {(True, 'aa', 123):  'def aa',
                                (True, 'bb', 2345): 'def bb'})

        tags = parser.parse('hello2.test')
        self.assertEqual(tags, {(True, 'cc', 1): 'def cc'})

    def test_parse_strip_punctuation(self):
        options = ParserOptions()
        options.strip_punctuation = True
        parser = CtagsParser('./ctags_stub.py', options)
        tags = parser.parse('punct.test')
        self.assertEqual(tags, {(True, '-_.', 123): 'def !"#$%&\'()*+,/:-_.;<=>?@[\\]^`{|}~'})

    def test_parse_no_strip_punctuation(self):
        options = ParserOptions()
        parser = CtagsParser('./ctags_stub.py', options)
        tags = parser.parse('punct.test')
        self.assertEqual(tags, {(True, '!"#$%&\'()*+,/:-_.;<=>?@[\\]^`{|}~', 123): 'def !"#$%&\'()*+,/:-_.;<=>?@[\\]^`{|}~'})

if __name__ == '__main__':
    unittest.main()
