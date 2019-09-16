#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import chain, combinations



def angryAnimals(n, a, b):
    
    all_animals = [i for i in range(1,n+1)]
    ## enemy pairs
    enemy_pairs = set(zip(a,b))
    ## find enemy combinations
    enemy_comb = (list(filter(lambda x: x if all(i in x for i in y) else None,\
    (chain(*map(lambda x: combinations(all_animals, x), range(1, len(all_animals)+1)))))) for y in enemy_pairs)
    
    enemy_comb = list(set((chain.from_iterable(enemy_comb))))

    ## remove enemy pairs from all combinations
    diff = list(set((chain(*map(lambda x: combinations(all_animals, x), range(1, len(all_animals)+1))))) - set(enemy_comb))

    ## remove groups that cannot be interval or contain consequent items
    tmp = [tuple(y for y in range(x[0], x[-1]+1)) for x in diff]
    res = set(x for x in tmp if x in enemy_comb)

    return len(res)

if __name__ == '__main__':
    import time
    start_time = time.time()
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ## number of animals
    n = int(input().strip())
    ## number of elements in array a
    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    ## number of elements in array b
    b_count = int(input().strip())

    b = []

    for _ in range(b_count):
        b_item = int(input().strip())
        b.append(b_item)

    len_result = angryAnimals(n, a, b)
    print("Time spent in seconds: ",time.time() - start_time)
#
#    fptr.write(str(result) + '\n')
#
#    fptr.close()
