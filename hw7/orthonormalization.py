import math
from orthogonalization import orthogonalize, aug_orthogonalize
from vecutil import *

def orthonormalize(L):
    '''
    Input: a list L of linearly independent Vecs
    Output: A list T of orthonormal Vecs such that for all i in [1, len(L)],
            Span L[:i] == Span T[:i]
    '''
    return [v/math.sqrt(v*v) for v in orthogonalize(L)]


def vec2list(vec):
    l = []
    for k in range(len(vec.D)):
        l.append(0 if k not in vec.f else vec.f[k])
    return l

def aug_orthonormalize(L):
    '''
    Input:
        - L: a list of Vecs
    Output:
        - A pair Qlist, Rlist such that:
            * coldict2mat(L) == coldict2mat(Qlist) * coldict2mat(Rlist)
            * Qlist = orthonormalize(L)
    '''
    Qlist, sigmavecs = aug_orthogonalize(L)
    multipliers = [math.sqrt(v*v) for v in Qlist]
    Rlist = []
    for vec in sigmavecs:
        Rlist.append(list2vec([a*b for a,b in zip(vec2list(vec), multipliers)]))
    Qlist = orthonormalize(Qlist)
    return (Qlist, Rlist)
    
