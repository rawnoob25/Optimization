###########################
# 6.0002 Problem Set 1b: Space Change




#================================
# Part B: Golden Eggs
#================================


"""
Both dp_make_weight_returnEggCounts() and dp_make_weight()
return the expected outputs for the target weight 99
using either the tuple (1, 5, 10, 20)
or the tuple (1, 5, 10, 25) as the egg weights. 
"""




def dp_make_weight_returnEggCounts(egg_weights, target, memo):
    """
    This function finds the specific counts of eggs in each egg-weight class to return
    and returns a dictionary that maps their values to their respective counts. Assumes there
    is an infinite supply of eggs and that there is always an egg of weight 1.
    
    memo is a dictionary that maps a tuple(len(egg_weights):int, target_weight: int) to
    a dictionary((egg_weight_class:int):(number_of_eggs_in_weight_class:int))
    
    Returns: a dictionary((egg_weight_class:int):(number_of_eggs_in_that_weightClass:int))
    """
    n = len(egg_weights)
    key = (n, target)
    if key in memo:
        return memo[key]
    if target == 0:
        memo[key] = {}
        return memo[key]
    item = egg_weights[n-1]
    if item<=target:
        theDictionary = dp_make_weight_returnEggCounts(egg_weights, target - item, memo)
        if item not in theDictionary:
            theDictionary[item]=1
        else:
            theDictionary[item]+=1
        memo[key] = theDictionary
    else: #item>target
        memo[key] = dp_make_weight_returnEggCounts(egg_weights[:(n-1)], target, memo)
        
    return memo[key]
        
        


# Problem 1
def dp_make_weight(egg_weights, target_weight, memo):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary that maps a tuple(len(egg_weights):int, target_weight:int) to the minimum number of eggs:int corresponding
    to that subarray and target weight.
    
    Returns: int, smallest number of eggs needed to make target weight
    
    >>> egg_weights = (1, 5, 10, 25)
    >>> dp_make_weight(egg_weights, 99, {})
    9
    >>> egg_weights = (1, 5, 10, 20)
    >>> egg_weights
    (1, 5, 10, 20)
    >>> dp_make_weight(egg_weights, 99, {}) #this doctest is failing and I'm unsure why
    10
    """
    # TODO: Your code here
    n = len(egg_weights)
    if (n, target_weight) in memo:
        return memo[(n, target_weight)]
    if target_weight == 0:
        memo[(n, target_weight)] = 0
        return memo[(n, target_weight)]
    item = egg_weights[n-1]
    if item<=target_weight:
        memo[(n, target_weight)] = 1+dp_make_weight(egg_weights, target_weight - item, memo)
    else: #item>target_weight
        memo[(n, target_weight)] = dp_make_weight(egg_weights[:(n-1)], target_weight, memo)
    return memo[(n, target_weight)]


if __name__ == '__main__':
#    egg_weights = (1, 5, 10, 25)
#    n = 99
#    print("Egg weights = ", egg_weights)
#    print("target = ",n)
#    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
#    print("Actual output:", dp_make_weight(egg_weights, n))
#    egg_weights = (1, 5, 10, 20)
#    n = 99
#    print("Egg weights = ", egg_weights)
#    print("target = ", n)
#    print("Expected output: 10(4 * 20 + 1 * 10 + 1 * 5 + 4 * 1")
#    print("Actual output:", dp_make_weight(egg_weights, n))
    print(dp_make_weight_returnEggCounts((1, 5, 10, 25), 99, {}))
    print(dp_make_weight_returnEggCounts((1, 5, 10, 20), 99, {}))