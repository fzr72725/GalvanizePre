import itertools
from collections import Counter
import math
from operator import mul
import numpy as np
from scipy.stats import binom,geom,poisson

def count_strings(string):
    '''
    INPUT: a string
    OUTPUT: an integer

    returns the number of distinct strings that can be made from the characters inside the argument string

    use itertools.permutations

    You should be able to use the function like this:
    >>> my_string = 'ab'
    >>> count_strings(my_string)
    2

    '''
    n = len(string)
    my_count = [math.factorial(value) for value in dict(Counter(string)).itervalues() if value > 1]
    return math.factorial(n)/reduce(mul,my_count,1)

import itertools

def make_fruit_salad(lst, k):
    '''
    return the list of possible combinations by taking k elements from lst

    use itertools.combinations

    You should be able to use the function like this:
    >>> my_fruits = ['pear', 'banana', 'apple']
    >>> make_fruit_salad(my_fruits, 2)
    [('pear', 'banana'), ('pear', 'apple'), ('banana', 'apple')]
    '''
    return [x for x in itertools.combinations(lst,k)]

def positive_test(TP, FP, perc_population):
      '''
      parameters
      ----------
      TP: true positive
          percentage of tests that were positive
          for the sample of subjects that had the disease
      FP: false positive
          percentage of tests that were positive
          for the control population (disease-free subjects)

      percent_population: percentage of the population that has the disease

      returns
      -------
      probability of having the disease for a person with a positive test result
      '''
      up = float(TP*perc_population)
      down = perc_population*TP+(1-perc_population)*FP
      #print down
      return up/down

def sales_pmf(appt1, appt2, deluxe_sale, std_cost, deluxe_cost):
    no_sale = 0
    results = [no_sale,no_sale,std_cost,std_cost,deluxe_cost,deluxe_cost]
    all_results = [sum(x) for x in itertools.permutations(results,2)]
    my_dict = {ar:0 for ar in all_results}
    for i in my_dict.iterkeys():
        if i == no_sale:
            my_dict[i]+= (1-appt1)*(1-appt2)
        if i == std_cost:
            my_dict[i]+= appt1*(1-deluxe_sale)*(1-appt2)+appt2*(1-deluxe_sale)*(1-appt1)
        if i == deluxe_cost:
            my_dict[i]+= appt1*deluxe_sale*(1-appt2)+appt2*deluxe_sale*(1-appt1)
        if i == std_cost+deluxe_cost:
            my_dict[i]+= appt1*(1-deluxe_sale)*appt2*deluxe_sale+appt2*(1-deluxe_sale)*appt1*deluxe_sale
        if i == std_cost*2:
            my_dict[i]+= appt1*(1-deluxe_sale)*appt2*(1-deluxe_sale)
        if i == deluxe_cost*2:
            my_dict[i]+= appt1*(deluxe_sale)*appt2*(deluxe_sale)
    return my_dict

def probability_rain(simulation_size=100000):
    '''
    choose the simulation_size

    returns
    -------
    probability that it will rain for at least two days in the next five days,
    knowing that the forecast says that in the next five days the chance of rain
    for each day is 25%
    '''
    n = 5
    p = 0.25
    rain = binom.rvs(n,p,size=simulation_size)
    return float(rain[np.where(rain>1)].size)/float(simulation_size)

def probability_coin(p=0.8):
  '''
  INPUT:
  p: probability of tails on a single flip of the coin (default 0.8)

  returns
  -------
  a dictionary showing the probability of first seeing a head on the kth flip,
  for k in range 1 to 15,
  knowing that you have an unfair coin,
  with an p chance of getting tails.
  '''
  k = 15
  return {i:round(geom.pmf(i,1-p),3) for i in xrange(1,k+1)}

def is_drug_effective(num_colds, l_drug, l_prior):
     '''
     num_colds: number of colds the person had over the 1 year period
     l_drug: parameter of a Poisson random variable that describes the number
     of times that a person contracts a cold in a given year taking the drug.
     l_prior: parameter of a Poisson random variable that describes the number
     of times that a person contracts a cold in a given year.

     use scipy.stats.poisson
     '''
     # Use Bayes Theorem
     p1 = poisson.pmf(num_colds,l_drug)*0.75
     p2 = poisson.pmf(num_colds,l_drug)*0.75+poisson.pmf(num_colds,l_prior)*0.25
     return p1/p2

if __name__ == '__main__':
    print is_drug_effective(num_colds, l_drug, l_prior)
