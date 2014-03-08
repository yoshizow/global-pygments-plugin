#!/usr/bin/env python

import optparse
import sys

RESPONSES = {
    'hello.test': [
        'aa 123 hello.test def aa',
        'bb 2345 hello.test def bb'
    ],
    'hello2.test': [
        'cc\t 1  \thello2.test\t \tdef cc'
    ],
    'punct.test': [
        '!"#$%&\'()*+,/:-_.;<=>?@[\\]^`{|}~ 123 punct.test def !"#$%&\'()*+,/:-_.;<=>?@[\\]^`{|}~'
    ]
}

opt_parser = optparse.OptionParser()
opt_parser.add_option('--filter-terminator', dest='filter_terminator')
opt_parser.add_option('-x', action='store_true')
opt_parser.add_option('-u', action='store_true')
opt_parser.add_option('--filter', action='store_true')
opt_parser.add_option('--format')
(options, args) = opt_parser.parse_args()
if not options.filter_terminator:
    opt_parser.error('--filter-terminator option not given')

while True:
    path = sys.stdin.readline()
    if not path:
        break
    path = path.rstrip()
    if path in RESPONSES:
        for line in RESPONSES[path]:
            print line
    print options.filter_terminator,
    sys.stdout.flush()
