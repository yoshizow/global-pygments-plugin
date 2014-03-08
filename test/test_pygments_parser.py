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
from mock import patch, mock_open
import pygments.lexers

sys.path.append('..')
from pygments_parser import *

class PygmentsParserTestCase(unittest.TestCase):
    @patch('pygments.lexers.get_lexer_by_name')
    def test_language_name_lowercased(self, mock_get_lexer_by_name):
        langmap = {'.rb': 'RuBY'}
        options = ParserOptions()
        parser = PygmentsParser(langmap, options)
        with patch('__builtin__.open', mock_open(read_data=''), create=True):
            parser.parse('hello.rb')
        mock_get_lexer_by_name.assert_called_once_with('ruby')

    @patch('pygments.lexers.get_lexer_by_name')
    def test_language_name_aliased(self, mock_get_lexer_by_name):
        langmap = {'.hx': 'HAxe'}
        options = ParserOptions()
        parser = PygmentsParser(langmap, options)
        with patch('__builtin__.open', mock_open(read_data=''), create=True):
            parser.parse('hello.hx')
        mock_get_lexer_by_name.assert_called_once_with('haXe')

    @patch('pygments.lexers.get_lexer_by_name')
    def test_parse(self, mock_get_lexer_by_name):
        tokens = iter([(0, Token.Name, 'a'),
                       (2, Token.Comment, 'b'),
                       (4, Token.Name, 'c')])
        mock_lexer = mock_get_lexer_by_name.return_value
        mock_lexer.get_tokens_unprocessed.return_value = tokens
        text = 'a\nb\nc\n'
        
        langmap = {'.test': 'Test'}
        options = ParserOptions()
        parser = PygmentsParser(langmap, options)
        with patch('__builtin__.open', mock_open(read_data=text), create=True):
            tags = parser.parse('hello.test')
            self.assertEqual(tags, {(False, 'a', 1): '',
                                    (False, 'c', 3): ''})

    @patch('pygments.lexers.get_lexer_by_name')
    def test_parse_no_newline_at_eof(self, mock_get_lexer_by_name):
        tokens = iter([(0, Token.Name, 'a'),
                       (2, Token.Comment, 'b'),
                       (4, Token.Name, 'c')])
        mock_lexer = mock_get_lexer_by_name.return_value
        mock_lexer.get_tokens_unprocessed.return_value = tokens
        text = 'a\nb\nc'
        
        langmap = {'.test': 'Test'}
        options = ParserOptions()
        parser = PygmentsParser(langmap, options)
        with patch('__builtin__.open', mock_open(read_data=text), create=True):
            tags = parser.parse('hello.test')
            self.assertEqual(tags, {(False, 'a', 1): '',
                                    (False, 'c', 3): ''})

    @patch('pygments.lexers.get_lexer_by_name')
    def test_parse_strip_punctuation(self, mock_get_lexer_by_name):
        tokens = iter([(0, Token.Name, '!"#$%&\'()*+,/:-_.;<=>?@[\\]^`{|}~')])
        mock_lexer = mock_get_lexer_by_name.return_value
        mock_lexer.get_tokens_unprocessed.return_value = tokens
        text = 'a'
        
        langmap = {'.test': 'Test'}
        options = ParserOptions()
        options.strip_punctuation = True
        parser = PygmentsParser(langmap, options)
        with patch('__builtin__.open', mock_open(read_data=text), create=True):
            tags = parser.parse('hello.test')
            self.assertEqual(tags, {(False, '-_.', 1): ''})

    @patch('pygments.lexers.get_lexer_by_name')
    def test_parse_no_strip_punctuation(self, mock_get_lexer_by_name):
        tokens = iter([(0, Token.Name, '!"#$%&\'()*+,/:-_.;<=>?@[\\]^`{|}~')])
        mock_lexer = mock_get_lexer_by_name.return_value
        mock_lexer.get_tokens_unprocessed.return_value = tokens
        text = 'a'
        
        langmap = {'.test': 'Test'}
        options = ParserOptions()
        parser = PygmentsParser(langmap, options)
        with patch('__builtin__.open', mock_open(read_data=text), create=True):
            tags = parser.parse('hello.test')
            self.assertEqual(tags, {(False, '!"#$%&\'()*+,/:-_.;<=>?@[\\]^`{|}~', 1): ''})

if __name__ == '__main__':
    unittest.main()
