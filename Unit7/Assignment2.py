import pickle
import numpy as np
import scipy.stats as scs

# Don't change this. This fixes the randomness in sampling
np.random.seed(seed=1234)


# This loads in the list of numbers you are going to deal with
def load_pickle(file_name):
    """INPUT:
    - file_name(STR) [The name of the file]

    OUTPUT:
    - population(NUMPY ARRAY) [A array of numbers for the exercise]
    """
    return pickle.load(open(file_name))


def draw_sample(population, n):
    """INPUT:
    - population(NUMPY ARRAY) [The array containing all the numbers]
    - n(INT) [The number of sample you wanna draw]

    OUTPUT:
    - sample(NUMPY ARRAY) [A array that contains a subset of the population]

    Hint: Use np.random.choice(). Google it. Google is your best friend
    """
    return np.random.choice(population,size=n)


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


if __name__ == '__main__':
    population = load_pickle('/Users/ziru/GalvanizePre/data/population.pkl')
    #print 'First 5 element of the population: ', population[:5]
    v100 = get_variance(draw_sample(population,100),sample=True)
    v1000 = get_variance(draw_sample(population,1000),sample=True)
    sem100 = get_sem(draw_sample(population,100))
    sem1000 = get_sem(draw_sample(population,1000))
    print 'Population Mean:',get_mean(population)
    print 'Sample 100 Mean:',get_mean(draw_sample(population,100))
    print 'Sample 1000 Mean:',get_mean(draw_sample(population,1000))
    print 'Population Var:',get_variance(population,sample=False)
    print 'Sample 100 Var:',v100
    print 'Sample 1000 Var:',v1000
    print 'Var Percentage Difference:',abs(v100-v1000)/((v100+v1000)*0.5)*100
    print 'Sample 100 Sem:',sem100
    print 'Sample 1000 Sem:',sem1000
    print 'Sem Percentage Difference:',abs(sem100-sem1000)/((sem100+sem1000)*0.5)*100
