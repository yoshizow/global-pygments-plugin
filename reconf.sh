#!/bin/sh
#
# Copyright (c) 2001, 2003, 2012 Tama Communications Corporation
# Copyright (c) 2014 Yoshitaro Makise
#
# This file is part of Pygments Plug-in Parser for GNU GLOBAL.
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
#
# Usage:
#
#	% sh reconf.sh [--configure|--make|--install]
#
case $1 in
--help)	echo "Usage: sh reconf.sh [--configure|--make|--install]"
	exit 0;;
esac
prog='autoconf automake m4'	# required programs
file='configure.ac Makefile.am libparser/parser.h'	# required files

case `uname` in
    Darwin*) prog="$prog glibtool" ;;
    *)       prog="$prog libtool" ;;
esac

echo "- File existent checking..."
for f in `echo $file`; do
	if [ ! -f $f ]; then
		echo "*** File '$f' not found."
		echo "You must execute this command at the root of GLOBAL source directory."
		exit 1
	fi
	echo "+ $f"
done

#
# Software tools which was used for making this package is written to 'BUILD_TOOLS' file.
#
cat <<! >BUILD_TOOLS
This software was made using the following build tools:

!
echo "- Program existent checking..."
for p in `echo $prog`; do
	found=0
	for d in `echo $PATH | sed -e 's/^:/.:/' -e 's/::/:.:/g' -e 's/:$/:./' -e 's/:/ /g'`
	do
		if [ -x $d/$p ]; then
			#echo "Found at $d/$p."
			found=1
			echo "+ $d/$p"
			break
		fi
	done
	case $found in
	0)	echo "*** Program '$p' not found."
		echo "Please install `echo $p | sed -e 's/autoreconf/automake and autoconf/' -e 's/glibtool/libtool/'`."
		exit 1;;
	esac
	case $p in
	perl)	;;
	*)	$p --version | head -n 1 >>BUILD_TOOLS;;
	esac
done

echo "- Clean up config.cache..."
rm -f config.cache

echo "- Generating configure items..."
(set -x; autoreconf --symlink --verbose --install) &&
case $1 in
'')	echo "You are ready to execute ./configure"
	;;
--debug)
	./configure CFLAGS='-g -p -Wall -DDEBUG'
	make -s
	;;
--warn)
	./configure CFLAGS='-g -O2 -Wall'
	make -s
	;;
-c|--configure|--make|--install)
	./configure
	;;
esac && case $1 in
--make)	make
	;;
--install)
	make install
	;;
esac
