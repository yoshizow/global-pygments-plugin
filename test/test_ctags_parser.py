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
