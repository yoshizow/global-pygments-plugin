import os
import sys
import re
import string
import optparse
import pygments
from pygments.token import Token
from pygments import lexers

# In most cases, lexers can be looked up with lowercase form of formal
# language names. This dictionary defines exceptions.
LANGUAGE_ALIASES = {
    'fantom':     'fan',
    'haxe':       'haXe',
    'sourcepawn': 'sp',
    'typescript': 'ts',
    'xbase':      'XBase'
}

# Symbol characters: all punctuation chars except some chars
SYMBOL_CHARACTERS = string.punctuation.translate(None, '-_.')

class PygmentsParser:
    class Options:
        def __init__(self):
            self.strip_symbol_chars = False

    class ContentParser:
        def __init__(self, path, text, lexer, options):
            self.path = path
            self.text = text
            self.lexer = lexer
            self.options = options
            self.lines_index = None

        def parse(self):
            self.lines_index = self.build_lines_index(self.text)
            tokens = self.lexer.get_tokens_unprocessed(self.text)
            self.parse_tokens(tokens)

        def build_lines_index(self, text):
            lines_index = []
            cur = 0
            while True:
                i = text.find('\n', cur)
                if i == -1:
                    break
                cur = i + 1
                lines_index.append(cur)
            lines_index.append(len(text))    # sentinel
            return lines_index

        def parse_tokens(self, tokens):
            cur_line = 0
            for index, tokentype, value in tokens:
                if tokentype in Token.Name:
                    while self.lines_index[cur_line] <= index:
                        cur_line += 1
                    typ = 'R'
                    image = ''
                    value = re.sub('\s+', '', value)    # remove newline
                    if self.options.strip_symbol_chars:
                        value = value.strip(SYMBOL_CHARACTERS)
                    if value:
                        print typ, value, cur_line + 1, self.path, image

    def __init__(self, langmap, options):
        self.langmap = langmap
        self.options = options

    def parse(self, path):
        lexer = self.get_lexer_by_langmap(path)
        if lexer:
            text = self.read_file(path)
            if text:
                parser = self.ContentParser(path, text, lexer, self.options)
                parser.parse()

    def get_lexer_by_langmap(self, path):
        ext = os.path.splitext(path)[1]
        lang = self.langmap[ext]
        if lang:
            name = lang.lower()
            if name in LANGUAGE_ALIASES:
                name = LANGUAGE_ALIASES[name]
            lexer = lexers.get_lexer_by_name(name)
            return lexer
        return None

    def read_file(self, path):
        try:
            with open(path, 'r') as f:
                text = f.read()
                return text
        except Exception as e:
            print >> sys.stderr, e
            return None

def parse_langmap(string):
    langmap = {}
    mappings = string.split(',')
    for mapping in mappings:
        lang, exts = mapping.split(':')
        if not lang[0].islower():  # skip lowercase, that is for builtin parser
            for ext in exts.split('.'):
                if ext:
                    langmap['.' + ext] = lang
    return langmap

def handle_requests(langmap, options):
    parser = PygmentsParser(langmap, options)
    while True:
        path = sys.stdin.readline()
        if not path:
            break
        path = path.rstrip()
        parser.parse(path)
        print '###terminator###'
        sys.stdout.flush()

def get_parser_options_from_env(parser_options):
    env = os.getenv('GTAGSPYGMENTSOPTS')
    if env:
        for s in env.split(','):
            s = s.strip()
            if s == 'stripsymbolchars':
                parser_options.strip_symbol_chars = True

opt_parser = optparse.OptionParser()
opt_parser.add_option('--langmap', dest='langmap')
(options, args) = opt_parser.parse_args()
if not options.langmap:
    opt_parser.error('--langmap option not given')
langmap = parse_langmap(options.langmap)
parser_options = PygmentsParser.Options()
get_parser_options_from_env(parser_options)
handle_requests(langmap, parser_options)
