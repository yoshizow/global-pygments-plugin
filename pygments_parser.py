import os
import sys
import re
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

def build_lines_index(text):
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

def is_definition_token(tokentype):
    if tokentype in Token.Name.Function or \
       tokentype in Token.Name.Class:
        return True
    else:
        return False

def get_line_image(line, lines_index, text):
    if line > 0:
        beg = lines_index[line - 1]
    else:
        beg = 0
    end = lines_index[line]
    image = text[beg:end].rstrip()
    return image

def parse_tokens(tokens, path, lines_index, text):
    cur_line = 0
    for index, tokentype, value in tokens:
        if tokentype in Token.Name:
            while lines_index[cur_line] <= index:
                cur_line += 1
            if is_definition_token(tokentype):
                typ = 'D'
                image = get_line_image(cur_line, lines_index, text)
            else:
                typ = 'R'
                image = ''
            value = re.sub('\s+', '', value)    # remove newline
            if value:
                print typ, value, cur_line + 1, path, image

def read_file(path):
    try:
        with open(path, 'r') as f:
            text = f.read()
            return text
    except Exception as e:
        print >> sys.stderr, e
        return None

def parse(path, langmap):
    lexer = get_lexer_by_langmap(path, langmap)
    if lexer:
        text = read_file(path)
        if text:
            lines_index = build_lines_index(text)
            tokens = lexer.get_tokens_unprocessed(text)
            parse_tokens(tokens, path, lines_index, text)

def handle_requests(langmap):
    while True:
        path = sys.stdin.readline()
        if not path:
            break
        path = path.rstrip()
        parse(path, langmap)
        print '###terminator###'
        sys.stdout.flush()

parser = OptionParser()
parser.add_option('--langmap', dest='langmap')
(options, args) = parser.parse_args()
if not options.langmap:
    parser.error('--langmap option not given')
langmap = parse_langmap(options.langmap)

handle_requests(langmap)
