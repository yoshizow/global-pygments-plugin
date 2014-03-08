dnl
dnl Configuration script for GLOBAL.
dnl Process this file with autoconf to produce a configure script.
dnl
dnl Copyright (c) 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2008, 2010,
dnl	2011, 2012, 2013
dnl	Tama Communications Corporation
dnl Copyright (c) 2014 Yoshitaro Makise
dnl
dnl This file is part of Pygments Plug-in Parser for GNU GLOBAL.
dnl
dnl This program is free software: you can redistribute it and/or modify
dnl it under the terms of the GNU General Public License as published by
dnl the Free Software Foundation, either version 3 of the License, or
dnl (at your option) any later version.
dnl 
dnl This program is distributed in the hope that it will be useful,
dnl but WITHOUT ANY WARRANTY; without even the implied warranty of
dnl MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
dnl GNU General Public License for more details.
dnl 
dnl You should have received a copy of the GNU General Public License
dnl along with this program.  If not, see <http://www.gnu.org/licenses/>.
dnl
AC_INIT([Pygments plug-in parser for GNU GLOBAL],[0.0.1])
AC_CONFIG_SRCDIR(libparser/parser.h)
AC_CONFIG_HEADERS([config.h:config-h.in])
AC_PREREQ(2.59)
AM_INIT_AUTOMAKE([1.9.3 gnu])

dnl Checks for programs.
AC_PROG_CC
AC_PROG_INSTALL
AC_PROG_MAKE_SET

AM_PATH_PYTHON([2.6])
AC_DEFINE_UNQUOTED(PYTHON, "$PYTHON", [Path to python executable.])
AC_SUBST(PYTHON)

AC_GNU_SOURCE

LT_PREREQ([2.2.6b])
dnl
dnl Because autoreconf up to version 2.59 doesn't know LT_INIT,
dnl we use the old name AC_PROG_LIBTOOL.
dnl
AC_PROG_LIBTOOL

# Checks for libraries.

# Checks for header files.
AC_CHECK_HEADERS([stdlib.h string.h strings.h unistd.h])

# Checks for typedefs, structures, and compiler characteristics.
AC_TYPE_PID_T
AC_TYPE_SIZE_T

# Checks for library functions.
AC_FUNC_FORK
AC_FUNC_MALLOC
AC_FUNC_REALLOC
AC_CHECK_FUNCS([dup2 strstr])

AC_DJGPP

dnl
dnl for gtags.conf and function layer plugin parser sample.
dnl
AC_MSG_CHECKING(for exuberant ctags program)
AC_ARG_WITH(exuberant-ctags,
[  --with-exuberant-ctags=PROGRAM  specify Exuberant Ctags program ],
[
	EXUBERANT_CTAGS="$withval"
        if test "$withval" = no; then
                AC_MSG_RESULT(no)
	else
                AC_MSG_RESULT([using $EXUBERANT_CTAGS])
	fi
],
[
	for d in `echo $PATH | sed -e 's/^:/.:/' -e 's/::/:.:/g' -e 's/:$/:./' -e 's/:/ /g'`
	do
		if test -x "$d/ctags" && (sh -c "'$d/ctags' --version" | grep "Exuberant Ctags") > /dev/null 2>&1; then
			withval="$d/ctags"
			break
		fi
	done
	if test "$withval" = ''; then
		AC_MSG_RESULT(no)
	else
		EXUBERANT_CTAGS="$withval"
		AC_MSG_RESULT([using $EXUBERANT_CTAGS])
	fi
])

AC_DEFINE_UNQUOTED(EXUBERANT_CTAGS, "$EXUBERANT_CTAGS", [Exuberant Ctags program.])
AC_SUBST(EXUBERANT_CTAGS)

AM_CPPFLAGS='-I$(top_srcdir)/libparser -DGTAGSDATADIR=\"$(datadir)/gtags\"'

AC_SUBST(AM_CPPFLAGS)

AC_CONFIG_FILES([Makefile
	pygments_parser.py
	libparser/Makefile
	plugin-factory/Makefile
	test/Makefile
])
AC_OUTPUT
