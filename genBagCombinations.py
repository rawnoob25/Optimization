# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 22:53:01 2017
"""

def gen1BagCombo(L):    
    for i in range(2**len(L)):
        out=[]
        for j in range(len(L)):
            if (i//(2**j))%2==1:
              out.append(L[j])
        yield out


def gen2BagCombo(L):
    for i in range(3**len(L)):
        out1, out2 = [], []
        for j in range(len(L)):
            if (i//(3**j))%3==1:
                out1.append(L[j])
            elif (i//(3**j))%3==2:
                out2.append(L[j])
            else:
                continue
        yield (out1,out2)


def testGen1BagCombo():
    l=[chr(x) for x in range(97,101)]
    comboGen = gen1BagCombo(l)
    for i in range(16):
        try:
            print(comboGen.__next__())        
        except StopIteration as e:
            print("Don't have "+str(i)+"th element")

def testGen2BagCombo():
    l = [chr(x) for x in range(97,101)]
    comboGen = gen2BagCombo(l)
    for i in range(100):
        try:
            print(i, comboGen.__next__())
        except StopIteration as e:
            print("Don't have "+str(i)+"th element")
testGen2BagCombo()

#testGen1BagCombo()
