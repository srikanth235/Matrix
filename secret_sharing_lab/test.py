import random
from vec import *
from vecutil import *
from independence import *
from GF2 import one
def getindependentvectors(size):
    counter = 0
    while True:
        result = []
        for i in range(size):
            result.append(list2vec([random.randint(0,1)*one for j in range(6)]))
        if is_independent(result):
            return result
        else:
            print("Failed attempt: "+str(counter))
            counter = counter + 1
        
def generate():
    while True:
        a=[Vec({0, 1, 2, 3, 4, 5},{0: one, 1:one, 2: 0, 3: one, 4: 0, 5: one})]+getindependentvectors(2)
        b=[Vec({0, 1, 2, 3, 4, 5},{0: one, 1: one, 2: 0, 3: 0, 4: 0, 5: one})]+getindependentvectors(2)
        if is_independent(a+b):
            break;
    counter = 0
    comb=[{0,1,2},{0,1,3},{0,2,3},{0,1,4},{0,3,4},{0,2,4},{1,2,3},{1,2,4},{2,3,4},{1,3,4}]
    a.reverse()
    b.reverse()
    while True:
        at = [list2vec([random.randint(0,1)*one for j in range(6)])]+[list2vec([random.randint(0,1)*one for j in range(6)])]
        bt = [list2vec([random.randint(0,1)*one for j in range(6)])]+[list2vec([random.randint(0,1)*one for j in range(6)])]
        a = at+a
        b = bt+b
        flag = 1
        for s in comb:
            l = [a[i-1] for i in s] +[b[i-1] for i in s]
            if not is_independent(l):
                for temp in at:
                    a.remove(temp)
                for temp in bt:
                    b.remove(temp)
                flag = 0
                break
        if flag:
            return a,b
a,b=generate()
#print(a[0])
#print(b[0])
for i in range(5):
    print(a[i])
    print(b[i])
