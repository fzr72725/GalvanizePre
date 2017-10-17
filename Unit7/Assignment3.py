from scipy.stats import t

def get_mean(lst):
    """INPUT:
    - lst(NUMPY ARRAY) [The array of numbers where we find the mean of]

    OUTPUT:
    - mean_value(FLOAT)

    Hint: Don't use np.mean().
    Then use np.mean(arr) to see if you got the same value
    """
    return float(sum(lst))/float(len(lst))

def get_variance(lst, sample=True):
    """INPUT:
    - lst(NUMPY ARRAY) [Either the sample or the population]
    - sample(BOOL) [True if sample variance, False if population variance]

    OUTPUT:
    - lst_variance(FLOAT) [Sample or population variance depending]
    """
    mean = get_mean(lst)
    r = [float((i-mean)**2) for i in lst]
    if sample:
        return sum(r)/float(len(lst)-1)
    return sum(r)/float(len(lst))


def get_sem(sample):
    """INPUT:
    - sample(NUMPY ARRAY)

    OUTPUT:
    - sem(FLOAT) [Standard Error Mean]
    """
    #population = load_pickle('/Users/ziru/GalvanizePre/data/population.pkl')
    mean = get_mean(sample)
    r = [float((i-mean)**2) for i in sample]
    #var = sum(r)/float(len(sample)-1)
    var = get_variance(sample)
    return var**0.5/len(sample)**0.5

def get_confidence_interval(sample, confidence=.95):
    '''
    hint: use scs.t.ppf(percentile)
    Parameters
    ----------
    sample : {numpy array}
    confidence : {float} desired confidence level (defaults to .95)

    Returns
    -------
    {tuple} (lower_bound_of_ci, upper_bound_of_ci)
    '''
    sample_mean = get_mean(sample)
    sem = get_sem(sample)
    df = len(sample)-1
    ci_u = sample_mean+t.ppf((1+confidence)*0.5,df)*sem
    ci_l = sample_mean-t.ppf((1+confidence)*0.5,df)*sem

if __name__ == '__main__':
    sample = [1,0,1,1,1,0,0,0,1]
    print get_confidence_interval(sample, confidence=.95)
