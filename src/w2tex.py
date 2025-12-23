
def write2tex(cols, rows, ifiles, ofile, options):
    gap = str(options['margin']) + 'pt'

    alph_offset = ord('b') - ord('a')
    nfiles      = len(ifiles)

    worktex = ofile
    op = open(worktex, mode='w')
    op.write(r'\documentclass[tikz,border=0pt]{standalone}'+'\n')
    op.write(r'\usepackage{graphicx}'+'\n')

    label_list = [None]*nfiles
    label      = 'a'
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
            work_label_inner = work_label_inner + [label_list[k]]
            k = k + 1
        work_label = work_label + [work_label_inner]
        print(work_label[i])

    print(work_label)
    loc = mklocation(work_label, cols, rows, nfiles, gap)

    op.write(r'\begin{tikzpicture}'+'\n')
    k = 0
    for i in range(rows):
        for j in range(cols):
            print(f'{k=}, {i=}, {j=}')
            op.write(r'\node[anchor=north west,inner sep=0] at '+f'({loc[i][j]["x"]},{loc[i][j]["y"]})'+r' {\usebox{' + label_list[k] + '}};'+'\n')
            if (k == nfiles-1):
                op.write(r'\end{tikzpicture}'+'\n')
                op.write(r'\end{document}'+'\n')
                op.close()
                return

            k = k + 1


def alph_update(curr, offset):
    if (curr == 'Z'):
        raise ValueError('Too many input files')

    if (curr == 'z'):
        return 'A'

    return chr(ord(curr) + offset)


def mklocation(label, cols, rows, nfiles, gap):
    print()
    x = '0'
    y = '0'
    k = 0
    loc = []
    for i in range(rows):
        loc_col = []
        for j in range(cols):
            print(f'{k=}, {i=}, {j=}, label={label[i][j]}')
            if (j == 0):
                x = '0'
            elif (j == 1):
                x = r'\wd'+label[i][j-1] + '+' + gap
            else:
                x = loc_col[j-1]['x'] + r'+\wd' + label[i][j-1] + '+' + gap

            if (i == 0):
                y = '0'
            elif (i == 1):
                y = r'-\ht'+label[i-1][j] + '-' + gap
            else:
                y = loc[i-1][j]['y'] + r'-\ht' + label[i-1][j] + '-' + gap

            loc_col = loc_col + [{'x': x, 'y': y}]
            #print(f'{"":2}{k=}[{i=},{j=}]:{loc[k]=}', end="")
            if (k == nfiles-1):
                loc = loc + [loc_col]
                return loc
            k = k + 1
        loc = loc + [loc_col]
        print(loc_col)

    return loc


