#!/usr/bin/env python
# encoding=utf-8

# created Mittwoch, 12. Dezember 2012 11:07 (C) 2012 by Leander Jedamus
# modifiziert Samstag, 04. Juli 2015 14:01 von Leander Jedamus
# modified Montag, 04. Februar 2013 16:52 by Leander Jedamus
# modified Montag, 28. Januar 2013 13:11 by Leander Jedamus
# modified Montag, 28. Januar 2013 13:06 by Leander Jedamus
# modified Montag, 31. Dezember 2012 08:28 by Leander Jedamus
# modified Mittwoch, 12. Dezember 2012 11:09 by Leander Jedamus

import vim
import pyvim as p

p.b()[0:0] = [ "",
               "// " + p.cb(),
	       "",
	       "// vim:ai sw=2"
             ]
vim.command("normal 2k")

# vim:ai sw=2 sts=4 expandtab

