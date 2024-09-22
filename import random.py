import random
import numpy as np


def crossover(chromosome_A, chromosome_B):
    n = len(chromosome_A)
    point1 = random.randint(0, n-2)
    point2 = random.randint(point1+1, n-1)
    child1 = [None]*n
    child2 = [None]*n

    child1[point1:point2] = chromosome_A[point1:point2]
    child2[point1:point2] = chromosome_B[point1:point2]
    print (f"point one is : {point1 } and the other one is {point2}")
    print (child1)
    print (child2)



    for i in range(n):
        if child1[i] == None:
            if chromosome_B[i] not in child1:
                child1[i] = chromosome_B[i]
        if child2[i] == None:
            if chromosome_A[i] not in child2:
                child2[i] = chromosome_A[i]           
    print (child1)
    print (child2)    

    for i in range(n):
        if child1[i] == None:
            for j in range(n):
                if j not in child1:
                    child1[i] = j
        if child2[i] == None:
            for j in range(n):
                if j not in child2: child2[i] = j
    print (child1)
    print (child2) 



numberOfRolls = 10
chromosome_A = np.array(random.sample(range(numberOfRolls),numberOfRolls))
chromosome_B = np.array(random.sample(range(numberOfRolls),numberOfRolls))

print(f"chromosome A :          {chromosome_A}")
print(f"chromosome B :          {chromosome_B}")

crossover(chromosome_A , chromosome_B)
