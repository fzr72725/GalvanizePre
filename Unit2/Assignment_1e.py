def string_combinations(alphabet, n):
    '''
    Use itertools.combinations to return all the combinations of letters in
    alphabet with length at most n.

    Parameters
    ----------
    alphabet : {str}
    n : {int}

    Returns
    -------
    list : {list} of {str}

    Example
    -------
    >>> string_combinations('abc', 2)
    ['a', 'b', 'c', 'ab', 'ac', 'bc']
    '''
    from itertools import combinations, chain
    return list(chain.from_iterable([[''.join(comb) for comb in combinations(list(alphabet),i)] for i in xrange(1,n+1)]))


def permutations_in_dict(string, words):
    '''
    Use itertools.permutations to return all the permutations of the string
    and return only the ones which are members of set words.

    Parameters
    ----------
    string : {str}
    words : {set}

    Returns
    -------
    list : {list} of {str}

    Example
    -------
    >>> permutations_in_dict('act', {'cat', 'rat', 'dog', 'act'})
    ['act', 'cat']
    '''
    from itertools import permutations
    return [''.join(perm) for perm in permutations(list(string)) if ''.join(perm) in words]
    if __name__ == '__main__':
        permutations_in_dict(string, words)
