def add(*lists: list):
    outer_list_lengths = set([len(i) for i in lists])
    inner_list_lengths = set([len(j) for i in lists for j in i])
    if not len(outer_list_lengths) == len(inner_list_lengths) == 1:
        raise ValueError("Given matrices are not the same size.")
    return [[sum(j) for j in zip(*i)] for i in zip(*lists)]
