def filter_words(word_list, letter):
    '''
    Use filter to return the words from word_list which start with letter.

    Parameters
    ----------
    word_list : {list} of words ({str})
    letter : {str}

    Returns
    -------
    list : {list} of words {str}

    Example
    -------
    >>> filter_words(["salumeria", "dandelion", "yamo", "doc loi", "rosamunde",
                      "beretta", "ike's", "delfina"], "d")
    ['dandelion', 'doc loi', 'delfina']
    '''
    return filter(lambda x: x[0]==letter, word_list)


def factors(num):
    '''
    Use filter to return all of the factors of num.

    Parameters
    ----------
    num : {int}

    Returns
    -------
    list : {list} of {int}

    Example
    -------
    >>> factors(15)
    [1, 3, 5, 15]
    '''
    return [n for n in xrange(1,num+1) if num%n==0]


def only_sorted(L):
    '''
    Use filter to return only the lists from L that are in sorted order.
    Hint: the all function may come in handy.

    Parameters
    ----------
    L : {list} of {list} of {int}

    Returns
    -------
    list : {list} of {list} of {int}

    Example
    -------
    >>> only_sorted([[3, 4, 5], [4, 3, 5], [5, 6, 3], [5, 6, 7]])
    [[3, 4, 5], [5, 6, 7]]
    '''
    return [e for e in L if e==sorted(e)]


def digits_to_num(digits):
    '''
    Use reduce to take a list of digits and return the number that they
    correspond to. Do not convert the integers to strings.

    Parameters
    ----------
    digits : {list} of {int}

    Returns
    -------
    int : {int}

    Example
    -------
    >>> digits_to_num([5, 0, 3, 8])
    5038
    '''
    return reduce(lambda total,x: total*10+x, digits, 0)


def intersection_of_sets(list_of_sets):
    '''
    Use reduce to take the intersection of a list of sets.
    Hint: the & operator takes the intersection of two sets.

    Parameters
    ----------
    list_of_sets : {list} of {set}

    Returns
    -------
    set : intersection of all sets in list_of_sets

    Example
    -------
    >>> intersection_of_sets([{1, 2, 3}, {2, 3, 4}, {2, 5}])
    set([2])
    '''
    return reduce(lambda inc,x: inc&x, list_of_sets,list_of_sets[0])
    if __name__ == '__main__':
        shift_on_character(string, char)
