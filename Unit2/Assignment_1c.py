def shift_on_character(string, char):
    '''
    Find the first occurence of the character char and return the string with
    everything before char moved to the end of the string. If char doesn't
    appear, return the same string.

    Parameters
    ----------
    string : {str}
    char : {str}

    Returns
    -------
    str

    Example
    -------
    >>> shift_on_character("galvanize", "n")
    'nizegalva'
    '''
    for i,e in enumerate(string):
        if e==char:
            return string[i:]+string[:i]
    return string


def is_palindrome(string):
    '''
    Return whether the given string is the same forwards and backwards.

    Parameters
    ----------
    string : {str

    Returns
    -------
    bool

    Example
    -------
    >>> is_palindrome("rats live on no evil star")
    True

    >>> is_palindrome("the moon waxes poetic in sunlight")
    False
    '''
    return string==string[::-1]


def alternate(L):
    '''
    Use list slicing to return a list containing all the odd indexed elements
    followed by all the even indexed elements.

    Parameters
    ----------
    L : {list}

    Returns
    -------
    list : {list}

    Example
    -------
    >>> alternate(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
    ['b', 'd', 'f', 'a', 'c', 'e', 'g']
    '''
    return [e for i,e in enumerate(L) if i%2!=0]+[e for i,e in enumerate(L) if i%2==0]


def shuffle(L):
    '''
    Return the result of a "perfect" shuffle. You may assume that L has even
    length. You should return the result of splitting L in half and alternating
    taking an element from each.

    Parameters
    ----------
    L : {list}

    Returns
    -------
    list : {list}

    Example
    -------
    >>> shuffle([1, 2, 3, 4, 5, 6])
    [1, 4, 2, 5, 3, 6]
    '''
    h_1 = L[:len(L)/2]
    h_2 = L[len(L)/2:]
    return list(reduce(lambda total,e: total+e, zip(h_1, h_2)))
    if __name__ == '__main__':
        shuffle(L)
