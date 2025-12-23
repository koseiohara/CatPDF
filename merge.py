import sys

def get_command(args_list):
    i = 0
    option_list = {}
    ifile_list  = []
    while (i < len(args_list)):
        if (args_list[i][0] == '-'):
            key    = args_list[i][1:]
            option = args_list[i+1][:]

            option_list[key] = option

            i = i + 1
        else:
            ifile_list = ifile_list + [args_list[i]]

        i = i + 1
    return ifile_list, option_list


def set_options(iopt):
    default = {
               'tile'  : 'horizontal',
               'margin': 0           ,
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
    elif (file == 'vertical' or tile == 'v'):
        cols = 1
        rows = len(ifile)
    elif ('x' in tile):
        x = tile.index('x')
    else:
        raise ValueError(f'Invalid tile format: 
        


args  = sys.argv[1:-1]
ofilr = args[-1]

ifile, opt = get_command(args)
opt = set_options(opt)

