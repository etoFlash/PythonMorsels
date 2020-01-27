def add(*args):
    len_list = sorted([len(sm) for sm in m]
                      for m in args)
    if len_list[0] != len_list[-1]:
        raise ValueError("Given matrices are not the same size.")

    len_params = len_list[0]
    matrix = []
    for i in range(len(len_params)):
        sub_matrix = []
        for j in range(len_params[i]):
            sub_matrix.append(sum(m[i][j] for m in args))
        matrix.append(sub_matrix)

    return matrix
