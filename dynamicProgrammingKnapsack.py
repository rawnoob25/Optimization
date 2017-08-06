# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 04:56:05 2017

prof_memoized_best(items:List<Item>, avail:int, d:dictionary<(int,int)->((),int))>, ct:int)
is a dynamic programming version of the brute force solution to the 0/1 knapsack problem.
It also keeps track of the number of recursive calls. 

The function test_prof_memoized_best() contains a unit test of prof_memoized_best()
with the same list of items and available weight constraint as the unit test for
the function prof_bestChoice_and_val() in bruteForceKnapsack.py. However,
that the brute force function uses 201 recursive calls, while this version (prof_memoized_best())
only uses 99.

In general, the extent of the advantage that the dynamic programming version of the
function affords over the pure brute force solution is dictated by the number
of overlapping subproblems.

"""


from bruteForceKnapsack import Item

def prof_memoized_best(items, avail, d, ct):
    """
    This is a profiled version of memoized_best (below) that keeps track of the 
    number of recursive calls spawned by (and including) the original recursive call.
    
    params: item is a list of Item instances- each of which has an integer field wt
    and an integer field value. avail is a nonnegative integer that represents
    the maximum allowable weight. d is a dictionary that's used as a memo. ct is a 
    single element list.
    
    return value: a two-element tuple, out; out[0] is a tuple consisting of
    elements in the highest-valued sublist of items such that total weight does
    not exceed avail; out[1] is the aggregate value of the elements in out[0] 
    """
    
    ct[0]+=1
    n=len(items)
    key=(n, avail)
    if key in d:
        return d[key]
    if n==0 or avail==0:
        d[key]=((),0)
        return d[key]
    
    first = items[0]
    
    if first.wt>avail:
        d[key] = prof_memoized_best(items[1:], avail, d, ct)
        return d[key]
    
    withFirst_items, withFirst_value = prof_memoized_best(items[1:], avail - first.wt, d, ct)
    withFirst_value += first.value
    
    withoutFirst_items, withoutFirst_value = prof_memoized_best(items[1:], avail, d, ct)
    
    if withFirst_value > withoutFirst_value:
        withFirst_items+=(first,)
        d[key] = (withFirst_items, withFirst_value)
        return d[key]
    else:
        d[key] = (withoutFirst_items, withoutFirst_value)
        return d[key]
    

def memoized_best(items, avail, d={}):
    """
    params: item is a list of Item instances- each of which has an integer field wt
    and an integer field value. avail is a nonnegative integer that represents
    the maximum allowable weight. d is a dictionary that's used as a memo.
    
    return value: a two-element tuple, out; out[0] is a tuple consisting of
    elements in the highest-valued sublist of items such that total weight does
    not exceed avail; out[1] is the aggregate value of the elements in out[0]
    """
    n=len(items)
    key=(n, avail)
    if key in d:
        return d[key]
    if n==0 or avail==0:
        d[key]=((),0)
        return d[key]
    
    first = items[0]
    
    if first.wt>avail:
        d[key] = memoized_best(items[1:], avail, d)
        return d[key]
    
    withFirst_items, withFirst_value = memoized_best(items[1:], avail - first.wt, d)
    withFirst_value += first.value
    
    withoutFirst_items, withoutFirst_value = memoized_best(items[1:], avail, d)
    
    if withFirst_value > withoutFirst_value:
        withFirst_items+=(first,)
        d[key] = (withFirst_items, withFirst_value)
        return d[key]
    else:
        d[key] = (withoutFirst_items, withoutFirst_value)
        return d[key]

def test_memoized_best():
    names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donut']
    vals = [89, 90, 95, 100, 90, 79, 50, 10]
    kcals = [123, 154, 258, 354, 365, 150, 95, 195]  
    assert len(vals) == len(kcals) and len(vals) == 8
    print("ADDING THE FOLLOWING ITEMS: wine, beer, pizza, burger, fries, cola, apple, donut")
    items=[]
    for i in range(len(vals)):
        items.append(Item(names[i], kcals[i], vals[i]))
    for item in items:
        print(item)
    print("Displaying the optimal selection of items to take")
    best = memoized_best(items, 750)
    print("Total value of items taken:"+str(best[1]))
    for e in best[0]:
        print(e)
        
def test_prof_memoized_best():
    names = [chr(x) for x in range(97,104)]
    wts = [3, 3, 2, 5, 7, 6, 4]
    vals = list(range(6,13))
    assert len(names)==len(wts) and len(wts)==len(vals)
    items=[]
    for i in range(len(names)):
        items.append(Item(names[i], wts[i], vals[i]))
    print("THE FULL LIST OF ITEMS IS:")
    for item in items:
        print(item)
    ct = [0]
    d={}
    best = prof_memoized_best(items, 18, d, ct)
    print("THE OPTIMAL SELECTION OF ITEMS TO TAKE IS:")
    for e in best[0]:
        print(e)    
    print("The aggregate value of these items is:"+str(best[1]))
    print("The number of recursive calls was:"+str(ct))
if __name__ == "__main__":
    test_prof_memoized_best()
