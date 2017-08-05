"""
This example is taken from the link: https://stackoverflow.com/questions/18035595/powersets-in-python-using-itertools
The response was on August 3'13 at 17:52 by Martijn Pieters.

The function powerset(iterable) 
returns a generator for the powerset on that iterable
"""

from itertools import chain, combinations
def powerset(iterable):
    '''
    Takes an iterable and returns a generator that is capable
    of yielding tuples- each of which consists of elements in
    a distinct subiterable of L
    
    >>> L=[1,2,3]
    >>> powerGen=powerset(L)
    >>> [e for e in powerGen]
    [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]
    '''
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def test_powerset():
    L=list("abcd")
    powerGen=powerset(L) #powerGen is a generator that yields tuples-
    #each of which contains elements in a distinct subiterable of L
    i=0
    for e in powerGen:
        print(e)
        i+=1
    assert i==2**len(L)
    print("--------")
    L=[1,2,3]
    powerGen=powerset(L)
    print([e for e in powerGen])
test_powerset()
