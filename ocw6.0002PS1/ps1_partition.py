#From codereview.stackexchange.com                    
def partitions(set_):
    if not set_:
        yield []
        return
    for i in range(2**len(set_)//2):
        parts = [set(), set()]
        for item in set_:
            parts[i&1].add(item)
            i >>= 1
        for b in partitions(parts[1]):
            yield [parts[0]]+b


# This is a helper function that will fetch all of the available 
# partitions for you to use for your brute force algorithm.
def get_partitions(set_):
    parts = partitions(set_)
    for partition in parts:
        yield [list(elt) for elt in partition]

if __name__ == "__main__":
    #a unit test of get_partitions()
    the_partitions = get_partitions(list("abcd"))
    print(type(the_partitions))
    
    i=0
    for item in the_partitions:
         i+=1   
         print(item)
    
    print("the_partitions has "+str(i)+" elements.")
