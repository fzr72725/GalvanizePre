def count_match_index(L):
    '''
    Use enumerate and other skills to return the count of the number
    of items in the list whose value equals its index.

    Parameters
    ----------
    L : {list} of {int}

    Returns
    -------
    int : {int}

    Example
    -------
    >>> count_match_index([0, 2, 2, 3, 6, 5])
    4
    '''
    return len([e for i,e in enumerate(L) if i==e])


def invert_list(L):
    '''
    Use enumerate and other skills to return a dictionary which has
    the values of the list as keys and the index as the value. You may assume
    that a value will only appear once in the given list.

    Parameters
    ----------
    L : {list}

    Returns
    -------
    dict : keys are entries in L, vallues are the index

    Example
    -------
    >>> invert_list(['a', 'b', 'c', 'd'])
    {'a': 0, 'c': 2, 'b': 1, 'd': 3}
    '''
    return {key:value for value,key in enumerate(L)}


def concatenate(L1, L2, connector=""):
    '''
    L1 and L2 have the same length. Use zip and other skills from above to
    return a list of the same length where each value is the two strings from
    L1 and L2 concatenated together with connector between them.

    Parameters
    ----------
    L1 : {list} of {str}
    L2 : {list} of {str}
    connector : {str} (optional)

    Returns
    -------
    list : {list} of {str}

    Example
    -------
    >>> concatenate(["A", "B"], ["b", "b"])
    ['Ab', 'Bb']
    >>> concatenate(["San Francisco", "New York", "Las Vegas", "Los Angeles"], \
                    ["California", "New York", "Nevada", "California"], ", ")
    ['San Francisco, California', 'New York, New York', 'Las Vegas, Nevada', 'Los Angeles, California']
    '''
    return [a+connector+b for a,b in zip(L1,L2)]


def transpose(mat):
    '''
    Return the transpose of the matrix. You may assume that the matrix is not
    empty. You can do this using a double for loop in a list comprehension.
    There is also a solution using zip.

    Parameters
    ----------
    mat : {list} of {list} of {int}

    Returns
    -------
    list : {list} of {list} of {int}

    Example
    -------
    >>> M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    >>> transpose(M)
    [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    '''
    return [[row[i] for row in mat] for i in xrange(len(mat[0]))]


def acronym(phrase):
    '''
    Given a phrase, return the associated acronym by breaking on spaces and
    concatenating the first letters of each word together capitalized.

    Parameters
    ----------
    phrase : {str}

    Returns
    -------
    str : {str}

    Example
    -------
    >>> acronym("data science immersive")
    'DSI'
    '''
    return ''.join([word[0].upper() for word in phrase.split(' ')])


def sort_by_ratio(L):
    '''
    Sort the list L by the ratio of the elements in the 2-tuples.
    For example, (1, 3) < (2, 4) since 1/3 < 2/4.
    Use the key parameter in the sort method.

    Parameters
    ----------
    L : {list} of 2-tuples ({tuple}) of {int}

    Returns
    -------
    None

    Example
    -------
    >>> L = [(2, 4), (8, 5), (1, 3), (9, 4), (3, 5)]
    >>> sort_by_ratio(L)
    >>> L
    [(1, 3), (2, 4), (3, 5), (8, 5), (9, 4)]
    '''
    L.sort(key = lambda x:x[0]/float(x[1]))
    if __name__ == '__main__':
        print sort_by_ratio(L)
