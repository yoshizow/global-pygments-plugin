import os
import sys
import re
import string
from optparse import OptionParser
import pygments
from pygments import lexers
from pygments.token import Token

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
            self.strip_symbol_chars = True

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
                if self.is_definition_token(tokentype):
                    typ = 'D'
                    image = self.get_line_image(cur_line)
                else:
                    typ = 'R'
                    image = ''
                value = re.sub('\s+', '', value)    # remove newline
                if self.options.strip_symbol_chars:
                    value = value.strip(SYMBOL_CHARACTERS)
                if value:
                    print typ, value, cur_line + 1, self.path, image

    def is_definition_token(self, tokentype):
        if tokentype in Token.Name.Function or \
           tokentype in Token.Name.Class:
            return True
        else:
            return False

    def get_line_image(self, line):
        if line > 0:
            beg = self.lines_index[line - 1]
        else:
            beg = 0
        end = self.lines_index[line]
        image = self.text[beg:end].rstrip()
        return image

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

def get_lexer_by_langmap(path, langmap):
    ext = os.path.splitext(path)[1]
    lang = langmap[ext]
    if lang:
        name = lang.lower()
        if name in LANGUAGE_ALIASES:
            name = LANGUAGE_ALIASES[name]
        lexer = lexers.get_lexer_by_name(name)
        return lexer
    return None

def read_file(path):
    try:
        with open(path, 'r') as f:
            text = f.read()
            return text
    except Exception as e:
        print >> sys.stderr, e
        return None

def handle_file(path, langmap, options):
    lexer = get_lexer_by_langmap(path, langmap)
    if lexer:
        text = read_file(path)
        if text:
            parser = PygmentsParser(path, text, lexer, options)
            parser.parse()

def handle_requests(langmap, options):
    while True:
        path = sys.stdin.readline()
        if not path:
            break
        path = path.rstrip()
        handle_file(path, langmap, options)
        print '###terminator###'
        sys.stdout.flush()

def get_parser_options_from_env(parser_options):
    env = os.getenv('GTAGSPYGMENTSOPTS')
    if env:
        for s in env.split(','):
            s = s.strip()
            if s == 'nostripsymbolchars':
                parser_options.strip_symbol_chars = False

opt_parser = OptionParser()
opt_parser.add_option('--langmap', dest='langmap')
(options, args) = opt_parser.parse_args()
if not options.langmap:
    opt_parser.error('--langmap option not given')
langmap = parse_langmap(options.langmap)
parser_options = PygmentsParser.Options()
get_parser_options_from_env(parser_options)
handle_requests(langmap, parser_options)
