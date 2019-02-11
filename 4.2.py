# Randomized algorithms

# hire-assistant problem
import math
import numpy as np
import matplotlib.pyplot as plt
def hire_assistant(n):
    hired = []
    best = 0
    # generate random order of applicants with random qualities
    applicants = np.random.random(n)
    # hire and fire
    for each in applicants:
        if each > best:
            best = each
            hired.append(best)
    return len(hired)
# hire_assistant(100)
def simulation(a,b,m):
    num_applicants = [i for i in range(1,a,b)]
    theo_hired = [math.log(i) for i in range(1,a,b) ]
    num_hired = []
    for i in range(1,a,b):
        count = 0
        for j in range(m):
            count += hire_assistant(i)
        average_i = count / m
        num_hired.append(average_i)
    plt.subplot(1,2,1)
    plt.plot(num_applicants, theo_hired)
    plt.subplot(1,2,2)
    plt.plot(num_applicants, num_hired)
    plt.show
#     return num_applicants, num_hired
simulation(1000,10,100)
        
"""
The probability of exactly 1 assistant being hired is: (n-1)! / (n!) = 1/n (since the first person in the list is best).
"""


# hat-check
import matplotlib.pyplot as plt
import random
def hat_check(n):
    # original hats and people
    people = [i for i in range(0,n)]
#     print(people)
    # hats given to people later on
    hats = random.sample(range(0,n),n)
#     print(hats)
    matched = 0
    # check if there is any match
    for i in range(n):
        if people[i] == hats[i]:
            matched += 1
    return matched
def simulation(a,b,m):
    num_people = [i for i in range(1,a,b)]
    theo_matched = []
    num_matched = []
    for i in range(1,a,b):
        count = 0
        for j in range(m):
            count += hat_check(i)
        average_i = count / m
        num_matched.append(average_i)
#     plt.subplot(1,2,1)
#     plt.plot(num_people, theo_matched)
    plt.subplot(1,2,2)
    plt.plot(num_people, num_matched)
    plt.show
    print(num_people, num_matched)
simulation(100,10,10)
