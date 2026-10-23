#!/usr/bin/env python3
"""Stamp a fresh build id into index.html (window.JOETOPIA_BUILD and every ?v= query) so browsers and
GitHub Pages' 10-minute cache never mix an old script or picture with a new release."""
import re, sys, time, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
build = sys.argv[1] if len(sys.argv) > 1 else time.strftime('%Y%m%d%H%M')
p = root / 'index.html'; s = p.read_text()
s = re.sub(r"JOETOPIA_BUILD = '[^']*'", f"JOETOPIA_BUILD = '{build}'", s)
s = re.sub(r'\?v=[A-Za-z0-9]+"', f'?v={build}"', s)
p.write_text(s); print('build', build)
