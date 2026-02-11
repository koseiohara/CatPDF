from pathlib import Path

def get_command(args_list):
    i = 0
    option_list = {}
    file_list   = []
    while (i < len(args_list)):
        if (args_list[i][0] == '-'):
            key    = args_list[i][1:]
            if (key == 'f'):
                option = True
            else:
                option = args_list[i+1][:]
                i = i + 1

            option_list[key] = option

        else:
            file_list = file_list + [args_list[i]]

        i = i + 1
    return file_list[:-1], file_list[-1], option_list


def get_ifile(ifiles):
    absolute = []
    for path in ifiles:
        pathp = Path(path)
        absolute = absolute + [str(pathp.resolve())]

    return absolute


def set_options(iopt):
    default = {
               'tile'  : 'horizontal',
               'margin': '0'         ,
               'align' : 'l'         ,
               'f'     : False       ,
              }
    options = default.copy()
    options.update(iopt)

    unknown = set(iopt) - set(default)
    if (unknown):
        unexpected = ', '.join(unknown)
        expected   = ', '.join(set(default))
        raise KeyError(f'Unexpected keyword(s): {unexpected}. Allowed keyword(s): {expected}')

    return options


def get_tile(tile, ifile):
    tile = tile.lower()
    if (tile == 'horizontal' or tile == 'h'):
        cols = len(ifile)
        rows = 1
    elif (tile == 'vertical' or tile == 'v'):
        cols = 1
        rows = len(ifile)
    elif ('x' in tile):
        x = tile.index('x')

        try:
            cols = int(tile[   : x])
            rows = int(tile[x+1:  ])
        except:
            raise ValueError(f'Invalid tile format: {tile}. Input should be "horizontal"/"h", "vertical"/"v", ' + 'or {columns}x{rows}.')
    else:
        raise ValueError(f'Invalid tile format: {tile}. Input should be "horizontal"/"h", "vertical"/"v", ' + 'or {columns}x{rows}.')

    if (cols*rows < len(ifile)):
        raise ValueError(f'Number of tiles is too small: {cols*rows}. {len(ifile)} files were specified.')

    return cols, rows


def get_margin(margin):
    margin = margin.lower()
    if ('x' in margin):
        x = margin.index('x')

        try:
            xmargin = int(margin[   :x])
            ymargin = int(margin[x+1: ])
        except:
            raise ValueError(f'Invalid margin format: {margin}. Input should be an integer, '+'or {width}x{height}.')
    else:
        try:
            xmargin = int(margin)
            ymargin = xmargin
        except:
            raise ValueError(f'Invalid margin format: {margin}. Input should be an integer, '+'or {width}x{height}.')
    
    return {'x': xmargin, 'y': ymargin}


def get_align(align):
    align = align.lower()
    if (align == 'left'):
        align = 'l'
    elif (align == 'center'):
        align = 'c'
    elif (align == 'right'):
        align = 'r'

    if (align != 'l' and align != 'c' and align != 'r'):
        raise ValueError(f'Invalid align input: {align}. align must be one of l (left), c (center), or r (right)')

    return align


def inquire(force, ifile, ofile):
    if (force):
        return

    print('Input Files:')
    for i in range(len(ifile)):
        print(f'{i+1:>6}. {ifile[i]}')

    print(f'Output File:\n{"":6s}{ofile}\n')
    inq_exec = input('Do you concatenate files? (y/n) ').strip().lower()

    if (inq_exec == 'y' or inq_exec == 'yes'):
        return
    else:
        exit(0)

