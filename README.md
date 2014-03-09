# Pygments Plug-in Parser for GNU GLOBAL

This software is a plug-in parser for GNU GLOBAL.
Uses Pygments, which is a syntax highlighter written in Python, to
extract tags.
Supports wide variety of programming languages thanks to Pygments.

This software can also use Exuberant Ctags.
When used only with Pygments, this plug-in parser generates only
symbol tags.
But when used with both Pygments and ctags, this parser can
generate both definition tags and reference tags.

## Prerequisites

- Python 2.6 or later (3.x is not supported)
- Pygments python package
- automake, autoconf
- gtags (GNU GLOBAL) 5.8.1 or later
- Exuberant Ctags 5.5 or later (optional)

## Install

Make sure Pygments package is installed.

    $ pip install Pygments

Generate automake/autoconf stuff.

    $ ./reconf.sh

Configure, build and install.

    # ./configure
    $ make
    $ sudo make install

Note:

- This software must be installed where gtags have been installed.
  For example, if you have installed gtags under `/opt/local`, you should
  run configure as `./confiure --prefix=/opt/local` .
- This software can work with Exuberant Ctags to extract definition
  tags.
  ctags is automatically detected by configure script.
  If you want to specify explicit location of ctags or want to
  disable ctags integration, you can pass `--with-exuberant-ctags=XXX`
  option to configure script.

## Configuration

Like other GLOBAL plug-in parsers, in order to use this plug-in parser,
you need to configure `~/.globalrc`.

First, write langmap entries for this plug-in.

    pygments-parser|Pygments plug-in parser:\
        :tc=common:\
        :langmap=ABAP\:.abap:\
        :langmap=ANTLR\:.G.g:\
        :langmap=ActionScript3\:.as:\
        :langmap=Ada\:.adb.ads.ada:\
        :langmap=AppleScript\:.applescript:\
        :langmap=AspectJ\:.aj:\
        :langmap=Aspx-cs\:.aspx.asax.ascx.ashx.asmx.axd:\
        :langmap=Asymptote\:.asy:\
        :langmap=AutoIt\:.au3:\
        :langmap=Awk\:.awk.gawk.mawk:\
        :langmap=BUGS\:.bug:\
        :langmap=Bash\:.sh.ksh.bash.ebuild.eclass:\
        :langmap=Bat\:.bat.cmd:\
        :langmap=BlitzMax\:.bmx:\
        :langmap=Boo\:.boo:\
        :langmap=Bro\:.bro:\
        :langmap=C#\:.cs:\
        :langmap=C++\:.c++.cc.cp.cpp.cxx.h.h++.hh.hp.hpp.hxx.C.H:\
        :langmap=COBOLFree\:.cbl.CBL:\
        :langmap=COBOL\:.cob.COB.cpy.CPY:\
        :langmap=CUDA\:.cu.cuh:\
        :langmap=C\:.c.h:\
        :langmap=Ceylon\:.ceylon:\
        :langmap=Cfm\:.cfm.cfml.cfc:\
        :langmap=Clojure\:.clj:\
        :langmap=CoffeeScript\:.coffee:\
        :langmap=Common-Lisp\:.cl.lisp.el:\
        :langmap=Coq\:.v:\
        :langmap=Croc\:.croc:\
        :langmap=Csh\:.tcsh.csh:\
        :langmap=Cython\:.pyx.pxd.pxi:\
        :langmap=Dart\:.dart:\
        :langmap=Dg\:.dg:\
        :langmap=Duel\:.duel.jbst:\
        :langmap=Dylan\:.dylan.dyl.intr:\
        :langmap=ECL\:.ecl:\
        :langmap=EC\:.ec.eh:\
        :langmap=ERB\:.erb:\
        :langmap=Elixir\:.ex.exs:\
        :langmap=Erlang\:.erl.hrl.es.escript:\
        :langmap=Evoque\:.evoque:\
        :langmap=FSharp\:.fs.fsi:\
        :langmap=Factor\:.factor:\
        :langmap=Fancy\:.fy.fancypack:\
        :langmap=Fantom\:.fan:\
        :langmap=Felix\:.flx.flxh:\
        :langmap=Fortran\:.f.f90.F.F90:\
        :langmap=GAS\:.s.S:\
        :langmap=GLSL\:.vert.frag.geo:\
        :langmap=Genshi\:.kid:\
        :langmap=Gherkin\:.feature:\
        :langmap=Gnuplot\:.plot.plt:\
        :langmap=Go\:.go:\
        :langmap=GoodData-CL\:.gdc:\
        :langmap=Gosu\:.gs.gsx.gsp.vark:\
        :langmap=Groovy\:.groovy:\
        :langmap=Gst\:.gst:\
        :langmap=HaXe\:.hx:\
        :langmap=Haml\:.haml:\
        :langmap=Haskell\:.hs:\
        :langmap=Hxml\:.hxml:\
        :langmap=Hybris\:.hy.hyb:\
        :langmap=IDL\:.pro:\
        :langmap=Io\:.io:\
        :langmap=Ioke\:.ik:\
        :langmap=JAGS\:.jag.bug:\
        :langmap=Jade\:.jade:\
        :langmap=JavaScript\:.js:\
        :langmap=Java\:.java:\
        :langmap=Jsp\:.jsp:\
        :langmap=Julia\:.jl:\
        :langmap=Koka\:.kk.kki:\
        :langmap=Kotlin\:.kt:\
        :langmap=LLVM\:.ll:\
        :langmap=Lasso\:.lasso:\
        :langmap=Literate-Haskell\:.lhs:\
        :langmap=LiveScript\:.ls:\
        :langmap=Logos\:.x.xi.xm.xmi:\
        :langmap=Logtalk\:.lgt:\
        :langmap=Lua\:.lua.wlua:\
        :langmap=MOOCode\:.moo:\
        :langmap=MXML\:.mxml:\
        :langmap=Mako\:.mao:\
        :langmap=Mason\:.m.mhtml.mc.mi:\
        :langmap=Matlab\:.m:\
        :langmap=Modelica\:.mo:\
        :langmap=Modula2\:.mod:\
        :langmap=Monkey\:.monkey:\
        :langmap=MoonScript\:.moon:\
        :langmap=MuPAD\:.mu:\
        :langmap=Myghty\:.myt:\
        :langmap=NASM\:.asm.ASM:\
        :langmap=NSIS\:.nsi.nsh:\
        :langmap=Nemerle\:.n:\
        :langmap=NewLisp\:.lsp.nl:\
        :langmap=Newspeak\:.ns2:\
        :langmap=Nimrod\:.nim.nimrod:\
        :langmap=OCaml\:.ml.mli.mll.mly:\
        :langmap=Objective-C++\:.mm.hh:\
        :langmap=Objective-C\:.m.h:\
        :langmap=Objective-J\:.j:\
        :langmap=Octave\:.m:\
        :langmap=Ooc\:.ooc:\
        :langmap=Opa\:.opa:\
        :langmap=OpenEdge\:.p.cls:\
        :langmap=PHP\:.php.php3.phtml:\
        :langmap=Pascal\:.pas:\
        :langmap=Perl\:.pl.pm:\
        :langmap=PostScript\:.ps.eps:\
        :langmap=PowerShell\:.ps1:\
        :langmap=Prolog\:.prolog.pro.pl:\
        :langmap=Python\:.py.pyw.sc.tac.sage:\
        :langmap=QML\:.qml:\
        :langmap=REBOL\:.r.r3:\
        :langmap=RHTML\:.rhtml:\
        :langmap=Racket\:.rkt.rktl:\
        :langmap=Ragel\:.rl:\
        :langmap=Redcode\:.cw:\
        :langmap=RobotFramework\:.robot:\
        :langmap=Ruby\:.rb.rbw.rake.gemspec.rbx.duby:\
        :langmap=Rust\:.rs.rc:\
        :langmap=S\:.S.R:\
        :langmap=Scala\:.scala:\
        :langmap=Scaml\:.scaml:\
        :langmap=Scheme\:.scm.ss:\
        :langmap=Scilab\:.sci.sce.tst:\
        :langmap=Smalltalk\:.st:\
        :langmap=Smarty\:.tpl:\
        :langmap=Sml\:.sml.sig.fun:\
        :langmap=Snobol\:.snobol:\
        :langmap=SourcePawn\:.sp:\
        :langmap=Spitfire\:.spt:\
        :langmap=Ssp\:.ssp:\
        :langmap=Stan\:.stan:\
        :langmap=SystemVerilog\:.sv.svh:\
        :langmap=Tcl\:.tcl:\
        :langmap=TeX\:.tex.aux.toc:\
        :langmap=Tea\:.tea:\
        :langmap=Treetop\:.treetop.tt:\
        :langmap=TypeScript\:.ts:\
        :langmap=UrbiScript\:.u:\
        :langmap=VB.net\:.vb.bas:\
        :langmap=VGL\:.rpf:\
        :langmap=Vala\:.vala.vapi:\
        :langmap=Velocity\:.vm.fhtml:\
        :langmap=Verilog\:.v:\
        :langmap=Vhdl\:.vhdl.vhd:\
        :langmap=Vim\:.vim:\
        :langmap=XBase\:.PRG.prg:\
        :langmap=XQuery\:.xqy.xquery.xq.xql.xqm:\
        :langmap=XSLT\:.xsl.xslt.xpl:\
        :langmap=Xtend\:.xtend:\
        :gtags_parser=ABAP\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=ANTLR\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=ActionScript3\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Ada\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=AppleScript\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=AspectJ\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Aspx-cs\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Asymptote\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=AutoIt\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Awk\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=BUGS\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Bash\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Bat\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=BlitzMax\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Boo\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Bro\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=C#\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=C++\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=COBOLFree\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=COBOL\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=CUDA\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=C\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Ceylon\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Cfm\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Clojure\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=CoffeeScript\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Common-Lisp\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Coq\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Croc\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Csh\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Cython\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Dart\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Dg\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Duel\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Dylan\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=ECL\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=EC\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=ERB\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Elixir\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Erlang\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Evoque\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=FSharp\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Factor\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Fancy\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Fantom\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Felix\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Fortran\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=GAS\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=GLSL\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Genshi\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Gherkin\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Gnuplot\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Go\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=GoodData-CL\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Gosu\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Groovy\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Gst\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=HaXe\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Haml\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Haskell\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Hxml\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Hybris\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=IDL\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Io\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Ioke\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=JAGS\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Jade\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=JavaScript\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Java\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Jsp\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Julia\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Koka\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Kotlin\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=LLVM\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Lasso\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Literate-Haskell\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=LiveScript\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Logos\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Logtalk\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Lua\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=MAQL\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=MOOCode\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=MXML\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Mako\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Mason\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Matlab\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=MiniD\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Modelica\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Modula2\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Monkey\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=MoonScript\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=MuPAD\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Myghty\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=NASM\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=NSIS\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Nemerle\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=NewLisp\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Newspeak\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Nimrod\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=OCaml\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Objective-C++\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Objective-C\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Objective-J\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Octave\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Ooc\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Opa\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=OpenEdge\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=PHP\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Pascal\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Perl\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=PostScript\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=PowerShell\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Prolog\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Python\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=QML\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=REBOL\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=RHTML\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Racket\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Ragel\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Redcode\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=RobotFramework\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Ruby\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Rust\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=S\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Scala\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Scaml\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Scheme\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Scilab\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Smalltalk\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Smarty\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Sml\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Snobol\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=SourcePawn\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Spitfire\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Ssp\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Stan\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=SystemVerilog\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Tcl\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=TeX\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Tea\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Treetop\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=TypeScript\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=UrbiScript\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=VB.net\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=VGL\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Vala\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Velocity\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Verilog\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Vhdl\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Vim\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=XBase\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=XQuery\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=XSLT\:/usr/local/lib/gtags/pygments-parser.la:\
        :gtags_parser=Xtend\:/usr/local/lib/gtags/pygments-parser.la:

This is so long, but you can remove unnecessary entries for you.
You can also add languages not listed here but Pygments supports.

Change path of `/usr/local/lib/gtags/pygments-parser.a` for the path
where you installed this plug-in.

Then, edit `default:` clause of `~/.globalrc` to use pygments-parser.
(Or you can configure this by setting environment variable GTAGSLABEL.)

     default:\
    -        :tc=native:
    +        :tc=native:tc=pygments:
    +pygments:\
    +:tc=pygments-parser:tc=htags:

Complete example is available at [sample.globalrc](sample.globalrc).

## Usage

Once you have configured ~/.globalrc, you can use gtags as usual.

    $ cat hello.rb
    class Hello
      def hello
        puts message
      end

      def message; 'hello, world'; end
    end
    $ gtags
    $ global -sx message hello.rb 
    message             3 hello.rb             puts message
    message             6 hello.rb           def message; 'hello, world'; end

As you can see 'message' in line 3 and line 6 are listed.
They are originally reference tag and definition tag respectively,
but they cannot be distinguished from Pygments's output,
so they are listed as symbol tags.

When ctags is installed, this parser call ctags to collect definition tags.
This enables distinguishing definition tags and reference tags.
Of course, this is only avaiable for programming languages which is
supported by ctags.

    $ cat hello.rb
    $ global -x message hello.rb 
    message             6 hello.rb         def message; 'hello, world'; end
    $ global -rx message hello.rb 
    message             3 hello.rb             puts message

You can see 'message' are listed as definition tag and reference tag.

### Customizing Behavior

Some programming languages allow punctuation characters in identifiers.
For example methods like gsub! or empty? in Ruby.
By default, this plug-in parser includes these kind of punctuation characters
in generated tags.
But for some GLOBAL front-ends (like gtags.el) this behavior is 
inconvenient.

In such case, you can set environment variable
`GTAGSPYGMENTSOPTS=strippunctuation` before running gtags to strip
punctuation characters from generated tags.

    $ cat hello.rb
    s = 'hello'
    s.gsub!(/./, '')
    s.empty?
    $ gtags
    $ gtags -d GRTAGS
    __.COMPACT   __.COMPACT
    __.COMPLINE  __.COMPLINE
    __.COMPNAME  __.COMPNAME
    __.VERSION   __.VERSION 6
    empty?  1 @n 3
    gsub!   1 @n 2
    s   1 @n 1-2
    $ export GTAGSPYGMENTSOPTS=strippunctuation
    $ gtags
    $ gtags -d GRTAGS
    __.COMPACT   __.COMPACT
    __.COMPLINE  __.COMPLINE
    __.COMPNAME  __.COMPNAME
    __.VERSION   __.VERSION 6
    empty   1 @n 3
    gsub    1 @n 2
    s   1 @n 1-2

## Limitations

This parser works for most programming languages supported by Pygments.
But for some languages it does not work well.  
For example, CoffeeScript lexer in Pygments 1.6 splits tokens in an
unusual manner. This may contribute to readability as a syntax
highlighter, but not work well with this software.

## Issues and Questions

If you have any issues or questions, please create an issue on GitHub.

https://github.com/yoshizow/global-pygments-plugin/issues

Pull requests are also welcome!

This product is depend on but not related to neither GNU GLOBAL,
Pygments nor Exuberant Ctags. Please don't ask them questions about
this software.

## Tested Environment

Tested with:

- Python 2.7.3
- Pygments 1.6
- autoconf 2.69
- automake 1.12.6
- global 6.2.9
- Exuberant Ctags 5.8

