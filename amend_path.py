#!/usr/bin/env python

import os

ghar_bin = os.path.join(
		os.path.abspath(os.path.dirname(__file__)),
		'bin')

export_line = "export PATH=$PATH:%s" % ghar_bin

dot_profile = os.path.join(os.getenv('HOME'), '.profile')
open(dot_profile, 'a').write("\n%s\n" % export_line)

print("To use ghar without restarting your shell, type: source ~/.profile")

