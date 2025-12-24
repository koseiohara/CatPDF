worktex=workdir+'worktex.tex'
workpdf=worktex[:-3]+'pdf'

import sys
import subprocess
from get_setting import get_command, set_options, get_tile, get_margin
from w2tex       import write2tex

args  = sys.argv[1:]

ifile, ofile, opt = get_command(args)
opt        = set_options(opt)
cols, rows = get_tile(opt['tile'], ifile)
margin     = get_margin(opt['margin'])

write2tex(cols, rows, margin, ifile, worktex, opt)

subprocess.run(f'cd {workdir}; latexmk -pdf {worktex}', shell=True)
subprocess.run(f'cp {workpdf} {ofile}', shell=True)


