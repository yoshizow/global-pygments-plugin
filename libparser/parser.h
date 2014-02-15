/*
 * Copyright (c) 2009, 2010
 *	Tama Communications Corporation
 *
 * This file is part of GNU GLOBAL.
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

#ifndef _PARSER_H_
#define _PARSER_H_

/*
 * Built-in parser base on gctags
 */

void parser_init(const char *, const char *);
void parser_exit(void);

/** @name tag type */
/** @{ */
			/** definition */
#define PARSER_DEF		1
			/** reference or other symbol */
#define PARSER_REF_SYM		2
/** @} */

/** @name flags */
/** @{ */
			/** debug mode */
#define PARSER_DEBUG		1
			/** verbose mode */
#define PARSER_VERBOSE		2
			/** print warning message */
#define PARSER_WARNING		4
			/** force level 1 block end */
#define PARSER_END_BLOCK	8
			/** force level 1 block start */
#define PARSER_BEGIN_BLOCK	16
/** @} */

typedef void (*PARSER_CALLBACK)(int, const char *, int, const char *, const char *, void *);

void parse_file(const char *, int, PARSER_CALLBACK, void *);

struct parser_param {
	int size;		/**< size of this structure */
	int flags;
	const char *file;
	PARSER_CALLBACK put;
	void *arg;
	int (*isnotfunction)(const char *);
	const char *langmap;
	void (*die)(const char *, ...);
	void (*warning)(const char *, ...);
	void (*message)(const char *, ...);
};

#endif
