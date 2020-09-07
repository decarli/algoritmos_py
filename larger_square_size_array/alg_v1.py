

def count(mat):
    cnt = 0
    for line in range(len(mat)):
        for column in range(len(mat)):
            total = count_seg_max_column(line, column, mat)

            if cnt < total:
                cnt = total

    print(f'QTD: {cnt}')

    return cnt


def count_seg_line(line, start_col, mat):
    qtd_col = 0

    for col in range(start_col, len(mat), 1):
        if mat[line][col] == 1:
            qtd_col = qtd_col + 1
        else:
            break

    return qtd_col


def count_seg_max_column(line, start_col, mat):
    qtd_col = count_seg_line(line, start_col, mat)
    if qtd_col == 0:
        return 0

    tot_cl = len(mat)

    for cl in range(start_col, start_col+qtd_col, 1):
        cl_tmp = 0

        for ln in range(line, line+qtd_col, 1):
            if ln >= len(mat):
                break

            if mat[ln][cl] == 1:
                cl_tmp = cl_tmp + 1

        if tot_cl > cl_tmp:
            tot_cl = cl_tmp

    return tot_cl
