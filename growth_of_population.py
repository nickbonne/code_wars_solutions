
# https://www.codewars.com/kata/growth-of-a-population/train/python

def nb_year(p0, percent, aug, p):

    population = p0
    years = 0

    while population < p:

        population = (population * (1 + (percent / 100))) + aug

        years += 1

    return years