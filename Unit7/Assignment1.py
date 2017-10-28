import numpy as np

def get_mean(lst):
    """
    INPUT: list of ints/floats
    RETURNS: the mean value of the input list as a float

    """
    return float(sum(lst))/float(len(lst))


def get_median(lst):
    """
    INPUT: list of ints/floats
    RETURNS: the median value of the input list as a float

    """
    lst.sort()
    if len(lst)%2 == 0:
        return float(lst[len(lst)/2-1]+lst[len(lst)/2])/2.0
    else:
        return lst[(len(lst)-1)/2]


def get_mode(lst):
    """
    INPUT: list of ints/floats
    RETURNS: the modal value of the input list as a float

    """
    my_dict = {}
    for i in lst:
        my_dict[i] = my_dict.get(i,0)+1
    return max(result, key = result.get)

def get_range(lst):
    """
    INPUT: list of ints/floats
    RETURNS: the range of the input list - the distance from the minimum value to the maximum value

    """
    lst.sort()
    return lst[len(lst)-1]-lst[0]


def get_IQR(lst):
    """
    INPUT: list of ints/floats
    RETURNS: the interquartile range of the input list - the distance from Q1 (25th percentile) to Q3 (75th percentile)

    hint: use [np.percentile](https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.percentile.html)

    """
    return np.percentile(lst,75)-np.percentile(lst,25)


def remove_outliers(lst):
    """
    INPUT: list of ints/floats
    RETURNS: two lists
              - a list of all data points that fall either 3 times the IQR above Q3
              or 3 times the IQR below Q1
              - a list of all remaining points

    """
    iqr = get_IQR(lst)
    q1 = np.percentile(lst,25)
    q3 = np.percentile(lst,75)
    l1 = [i for i in lst if ((abs(i-q3)>3*iqr)|(abs(q1-i)>3*iqr))]
    l2 = [i for i in lst if i not in l1]
    return l1,l2

if __name__ == '__main__':
    get_IQR(lst)
