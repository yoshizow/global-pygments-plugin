#!/usr/bin/env python
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
