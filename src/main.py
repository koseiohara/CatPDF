worktex=workdir+'worktex.tex'
workpdf=worktex[:-3]+'pdf'

import sys
import subprocess
from get_setting import get_command, set_options, get_tile
from w2tex       import write2tex

args  = sys.argv[1:]

ifile, ofile, opt = get_command(args)
print(f'{ifile=}')
print(f'{ofile=}')
print(f'{opt=}')
opt = set_options(opt)
cols, rows = get_tile(opt['tile'], ifile)

write2tex(cols, rows, ifile, worktex, opt)

subprocess.run(f'cd {workdir}; latexmk -pdf {worktex}', shell=True)
subprocess.run(f'cp {workpdf} {ofile}', shell=True)


