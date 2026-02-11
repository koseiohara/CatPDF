
def write2tex(cols, rows, margin, last_align, ifiles, ofile, options):
    #gap  = str(options['margin']) + 'pt'
    xgap = str(margin['x']) + 'pt'
    ygap = str(margin['y']) + 'pt'

    alph_offset  = ord('b') - ord('a')
    nfiles       = len(ifiles)
    protruded    = nfiles % cols
    align_center = (last_align == 'c') & (protruded != 0)
    align_right  = (last_align == 'r') & (protruded != 0)

    rows = min(rows, int(nfiles/cols)+1)
    print(f'DEBUG: {rows=}')

    worktex = ofile
    op = open(worktex, mode='w')
    op.write(r'\documentclass[tikz,border=0pt]{standalone}'+'\n')
    op.write(r'\usepackage{graphicx}'+'\n')

    label_list = [None]*nfiles
    label      = 'aaaa'
    for i in range(nfiles):
        label_list[i] = r'\fig' + label
        op.write(r'\newsavebox{'+label_list[i]+'}'+'\n')

        label = alph_update(label, alph_offset)

    op.write(r'\begin{document}'+'\n')
    for i in range(nfiles):
        op.write(r'\sbox{'+label_list[i]+'}{\includegraphics{'+ifiles[i]+'}}'+'\n')

    label_list = label_list + [None]*(cols*rows-nfiles)
    work_label = []
    k = 0
    for i in range(rows):
        work_label_inner = []
        for j in range(cols):
            if (label_list[k] is not None):
                work_label_inner = work_label_inner + [label_list[k]]
            k = k + 1
        work_label = work_label + [work_label_inner]

    loc = mklocation(work_label, cols, rows, nfiles, xgap, ygap)

    op.write(r'\newdimen\maxrowwidth'+'\n')
    # op.write(r'\newdimen\rowwidth'+'\n')
    op.write(r'\newdimen\rowwidth'+'\n')
    op.write(r'\newdimen\offset'+'\n')
    op.write(r'\maxrowwidth=0pt'+'\n')
    op.write(r'\rowwidth=0pt'+'\n')
    op.write(r'\offset=0pt'+'\n')
    op.write(r'\def\xgap{'+xgap+'}\n')

    rowwidth = [None]*rows
    # Loop in Row Direction
    for labidx in range(rows):
        labels = work_label[labidx]
        rowwidth_maker = r'\rowwidth=\dimexpr'
        # op.write(r'\rowwidth=\dimexpr')
        # Loop in Column Direction
        for figidx in range(len(labels)):
            rowwidth_maker = rowwidth_maker + r'\wd'+labels[figidx]
            # op.write(r'\wd'+labels[figidx])
            if (figidx < len(labels)-1): 
                rowwidth_maker = rowwidth_maker + r'+\xgap+'
                # op.write(r'+\xgap+')
            else:
                rowwidth_maker = rowwidth_maker + r'\relax'+'\n'
                # op.write(r'\relax'+'\n')

        op.write(rowwidth_maker)
        op.write(r'\ifdim\rowwidth>\maxrowwidth\maxrowwidth=\rowwidth\fi'+'\n')
        rowwidth[labidx] = rowwidth_maker

    op.write(r'\begin{tikzpicture}'+'\n')

    # labels = work_label[rows-1]
    # # print(f'DEBUG: labels={labels}')
    # op.write(r'\rowwidth=\dimexpr')
    # for figidx in range(len(labels)):   # NOTE: Do NOT change len(labels) to cols! The size of the last line may be smaller than cols!
    #     op.write(r'\wd'+labels[figidx])
    #     if (figidx < len(labels)-1): 
    #         op.write(r'+\xgap+')
    #     else:
    #         op.write(r'\relax'+'\n')

    if (align_center):
        define_offset = r'\offset=\dimexpr(\maxrowwidth-\rowwidth)/2\relax'+'\n'
    elif (align_right):
        define_offset = r'\offset=\dimexpr\maxrowwidth-\rowwidth\relax'+'\n'
    else:
        define_offset = r'\offset=0\relax'+'\n'

    k = 0
    for i in range(rows):
        op.write(rowwidth[i])
        op.write(define_offset)
        op.write(r'\ifdim\offset<0pt\offset=0pt\fi'+'\n')

        for j in range(cols):
            # op.write(r'\node[anchor=north west,inner sep=0] at '+f'({loc[i][j]["x"]},{loc[i][j]["y"]})'+r' {\usebox{' + label_list[k] + '}};'+'\n')
            op.write(r'\node[anchor=north west,inner sep=0] at (\offset+' + f'{loc[i][j]["x"]},{loc[i][j]["y"]})'+r' {\usebox{' + label_list[k] + '}};'+'\n')

            # if (i < rows-1):
            #     op.write(f'{loc[i][j]["x"]},{loc[i][j]["y"]})'+r' {\usebox{' + label_list[k] + '}};'+'\n')
            # else:
            # op.write(r'\offset+' + f'{loc[i][j]["x"]},{loc[i][j]["y"]})'+r' {\usebox{' + label_list[k] + '}};'+'\n')
            if (k == nfiles-1):
                op.write(r'\end{tikzpicture}'+'\n')
                op.write(r'\end{document}'+'\n')
                op.close()
                return

            k = k + 1


def alph_update(curr, offset):
    curr = list(curr)
    nstr = len(curr)
    for i in range(nstr):
        if (curr[nstr-i-1] != 'z'):
            curr[nstr-i-1] = chr(ord(curr[nstr-i-1]) + offset)
            curr[nstr-i:] = ['a']*i
            return ''.join(curr)

    raise ValueError('Too many input files')


def mklocation(label, cols, rows, nfiles, xgap, ygap):
    x = '0'
    y = '0'
    k = 0
    loc = []
    for i in range(rows):
        loc_col = []
        for j in range(cols):
            if (j == 0):
                x = '0'
            elif (j == 1):
                x = r'\wd'+label[i][j-1] + '+' + xgap
            else:
                x = loc_col[j-1]['x'] + r'+\wd' + label[i][j-1] + '+' + xgap

            if (i == 0):
                y = '0'
            elif (i == 1):
                y = r'-\ht'+label[i-1][j] + '-' + ygap
            else:
                y = loc[i-1][j]['y'] + r'-\ht' + label[i-1][j] + '-' + ygap

            loc_col = loc_col + [{'x': x, 'y': y}]
            if (k == nfiles-1):
                # if the location of the last file is fixed:
                loc = loc + [loc_col]
                return loc
            k = k + 1
        loc = loc + [loc_col]

    return loc


