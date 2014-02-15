AC_DEFUN([AC_DJGPP],
[AC_CACHE_CHECK([whether we are using the GNU DJGPP compiler], ac_cv_djgpp,
[AC_COMPILE_IFELSE([AC_LANG_PROGRAM([[]], [[#ifdef __DJGPP__
int a;
#else
XXXXXX
#endif]])],[ac_cv_djgpp=yes],[ac_cv_djgpp=no])])
AM_CONDITIONAL(DJGPP, test $ac_cv_djgpp = yes)
])
