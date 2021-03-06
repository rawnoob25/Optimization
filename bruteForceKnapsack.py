# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 21:14:40 2017

"""

class Item:
    """
    An Item has a description:string, wt:int, and value:int
    """
    
    def __init__(self, description, wt, value):
        self.description=description
        self.wt=wt
        self.value=value
    
    def __str__(self):
        return "("+self.description+" "+"wt:"+str(self.wt)+", value:"+str(self.value)+")"


#class Person(object):
#      
#      def __init__(self, name):
#          self.name = name
#          try:
#              lastBlank = name.rindex(' ')
#              self.lastName = name[lastBlank+1:]
#          except:
#              self.lastName = name
#          self.birthday = None
#      
#      def __str__(self):
#          return self.name

    
def test_Item():
    beer=Item("beer",145,90)
    pizza=Item("pizza",258,30)
    burger=Item("burger",354,50)
    items=[]
    items.append(beer)
    items.append(pizza)
    items.append(burger)
    for item in items:
        print(item)
    
 
def test_person():
    me = Person('Michael Guttag')
    print(me)


def prof_bestChoice_and_val(items, avail, ct):
    """
    Note: this is a profiled version of function bestChoice_and_val that
    keeps track of the number of recursive calls spawned from (and including)
    the original call
    
    params: item is a list of Item instances- each of which has an integer field wt
    and an integer field value. avail is a nonnegative integer that represents
    the maximum allowable weight. ct is a single-element list.
    
    return value: a two-element tuple, out; out[0] is a tuple consisting of
    elements in the highest-valued sublist of items such that total weight does
    not exceed avail; out[1] is the aggregate value of the elements in out[0]
    """    
    ct[0]+=1
    if items==[] or avail==0:
        return ((),0)
    if items[0].wt>avail:
        return prof_bestChoice_and_val(items[1:], avail, ct)
    
    #consider the best value resulting from choosing to take items[0]
    #and also consider the best value resulting from choosing NOT
    #to take items[0]; if the best value resulting from choosing
    #to take items[0] exceeds that from choosing NOT to take
    #items[0], include items[0] and its corresponding value
    #in the returned result; otherwise don't include items[0]
    #or its corresponding value in the returned result
    with_items, with_val = prof_bestChoice_and_val(items[1:], avail - items[0].wt, ct)
    with_val+=items[0].value
    
    without_items, without_val = prof_bestChoice_and_val(items[1:], avail, ct)
    if with_val > without_val:
        with_items+=(items[0],)
        return (with_items, with_val)
    else:
        return (without_items, without_val)

def bestChoice_and_val(items, avail):
    """
    params: item is a list of Item instances- each of which has an integer field wt
    and an integer field value. avail is a nonnegative integer that represents
    the maximum allowable weight.
    
    return value: a two-element tuple, out; out[0] is a tuple consisting of
    elements in the highest-valued sublist of items such that total weight does
    not exceed avail; out[1] is the aggregate value of the elements in out[0]
    """
    if items==[] or avail==0:
        return ((),0)
    if items[0].wt>avail:
        return bestChoice_and_val(items[1:], avail)
    
    #consider the best value resulting from choosing to take items[0]
    #and also consider the best value resulting from choosing NOT
    #to take items[0]; if the best value resulting from choosing
    #to take items[0] exceeds that from choosing NOT to take
    #items[0], include items[0] and its corresponding value
    #in the returned result; otherwise don't include items[0]
    #or its corresponding value in the returned result
    with_items, with_val = bestChoice_and_val(items[1:], avail - items[0].wt)
    with_val+=items[0].value
    
    without_items, without_val = bestChoice_and_val(items[1:], avail)
    if with_val > without_val:
        with_items+=(items[0],)
        return (with_items, with_val)
    else:
        return (without_items, without_val)

def testBestChoice_and_val():
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
    best = bestChoice_and_val(items, 750)
    print("Total value of items taken:"+str(best[1]))
    for e in best[0]:
        print(e)

def test_prof_bestChoice_and_val():
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
    best = prof_bestChoice_and_val(items, 18, ct)
    print("THE OPTIMAL SELECTION OF ITEMS TO TAKE IS:")
    for e in best[0]:
        print(e)
    
    #for e in best[0]:
    #    print(e)
    print("The aggregate value of these items is:"+str(best[1]))
    print("The number of recursive calls was:"+str(ct))

#test_person()
#print("----------------")
#test_Item()
if __name__ == "__main__":
        test_prof_bestChoice_and_val()