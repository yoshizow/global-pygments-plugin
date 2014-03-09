## Process this file with automake to create Makefile.in
#
# Copyright (c) 2000, 2001, 2002 Tama Communications Corporation
# Copyright (c) 2014 Yoshitaro Makise
#
# This file is free software; as a special exception the author gives
# unlimited permission to copy and/or distribute it, with or without
# modifications, as long as this notice is preserved.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY, to the extent permitted by law; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
SUBDIRS = libparser plugin-factory test

gtagsdir = ${datadir}/gtags
gtags_DATA = pygments_parser.py

EXTRA_DIST = ${gtags_DATA} reconf.sh sample.globalrc

install-data-hook:
	if cd $(DESTDIR)$(datadir)/gtags; then \
		chmod 755 pygments_parser.py; \
	fi
