worktex=workdir+'worktex.tex'
workpdf=worktex[:-3]+'pdf'

import sys
import subprocess
from get_setting import get_command, get_ifile, set_options, get_tile, get_margin, inquire
from w2tex       import write2tex

args  = sys.argv[1:]

ifile, ofile, opt = get_command(args)
opt        = set_options(opt)
inquire(opt['f'], ifile, ofile)

ifile      = get_ifile(ifile)
cols, rows = get_tile(opt['tile'], ifile)
margin     = get_margin(opt['margin'])

write2tex(cols, rows, margin, ifile, worktex, opt)

subprocess.run(f'cd {workdir}; latexmk -C', shell=True)
subprocess.run(f'cd {workdir}; latexmk -pdf {worktex}', shell=True)
subprocess.run(f'cp {workpdf} {ofile}', shell=True)


