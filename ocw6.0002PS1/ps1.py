###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    import heapq
    remaining=[]
    for c in cows.keys():
        remaining.append(c)
    out=[]
    while len(remaining)>0:
        thisTrip=[]
        pq=[]
        for e in remaining:
            heapq.heappush(pq,(-1*cows[e],e))
        left=limit
        while pq:
            front=heapq.heappop(pq)
            wt=-1*front[0]
            if wt<=left:
                left-=wt
                thisTrip.append(front[1])
                remaining.remove(front[1])
            if left==0:
                break
        out.append(thisTrip)
    return out
        


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    items = set(cows.keys())
    partitions = get_partitions(items)
    for e in partitions: #loop over the partitions supplied by the generator, partitions
        for trip in e: #loop over the trips (lists) in a partition (a partition is a list of lists)
            if not processTrip(trip, cows, limit):
                break
        else:
            return e

def processTrip(trip, d, limit):
    """
    params: trip is a list of strings that are keys in dictionary d; d is a dictionary(string->int);
    limit is an int
    
    returns: true if and only if the sum(d[k] for k in trip)<=limit
    """
    totalWt = 0
    for cow in trip:
        totalWt+=d[cow]
        if totalWt>limit:
            return False
    return True
        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    start = time.time()
    for i in range(1000):
        greedy_cow_transport(cows)
    end = time.time()
    #print("The number of trips returned by the greedy method was: "+str(len(greedy)))
    print("The execution time for greedy was:"+str(end - start))
    
    start = time.time()
    for i in range(1000):
        brute_force_cow_transport(cows)
    end = time.time()
    #print("The number of trips returned by the brute force method was:"+str(len(brute)))
    print("The execution time for brute was:"+str(end - start))
    

"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("smallDictionary.txt")
limit=10
#print(cows)

#print(greedy_cow_transport(cows, limit))
#print(brute_force_cow_transport(cows, limit))
#print(brute_force_cow_transport(cows))
compare_cow_transport_algorithms()

