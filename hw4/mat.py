from vec import Vec

def getitem(M, k):
    "Returns the value of entry k in M.  The value of k should be a pair."
    assert k[0] in M.D[0] and k[1] in M.D[1]
    return (M.f)[k] if k in M.f else 0

def setitem(M, k, val):
    "Sets the element of v with label k to be val.  The value of k should be a pair"
    assert k[0] in M.D[0] and k[1] in M.D[1]
    M.f[k] = val
    return

def add(A, B):
    "Returns the sum of A and B"
    assert A.D == B.D
    result = Mat(A.D, {})
    for k,v in A.f.items():
        result.f[k] = v
    for k,v in B.f.items():
        if k in result.f:
            result.f[k] = result.f[k] + v
        else:
            result.f[k] = v
    return result

def scalar_mul(M, alpha):
    "Returns the product of scalar alpha with M" 
    result = Mat(M.D, {})
    for k,v in M.f.items():
        result.f[k] = alpha*v
    return result

def equal(A, B):
    "Returns true iff A is equal to B"
    assert A.D == B.D
    for r in A.D[0]:
        for c in A.D[1]:
            if getitem(A, (r,c)) != getitem(B, (r,c)):
                return False
    return True

def transpose(M):
    "Returns the transpose of M"
    result = Mat((M.D[1], M.D[0]),{})
    result.f = {(k[1],k[0]):v for k,v in M.f.items()}
    return result

def vector_matrix_mul(v, M):
    "Returns the product of vector v and matrix M"
    assert M.D[0] == v.D
    if v.D == M.D[0]:
        result = Vec(M.D[1], {c:0 for c in M.D[1]})
        for k,value in M.f.items():
            if k[0] in v.f:
                result.f[k[1]] += v.f[k[0]]*value
    return result

def matrix_vector_mul(M, v):
    "Returns the product of matrix M and vector v"
    assert M.D[1] == v.D
    result = Vec(M.D[0], {r:0 for r in M.D[0]})
    for k, value in M.f.items():
        if k[1] in v.f:
            result.f[k[0]] += v.f[k[1]]*value
    return result

def matrix_matrix_mul(A, B):
    "Returns the product of A and B"
    assert A.D[1] == B.D[0]
    result = Mat((A.D[0],B.D[1]),{})
    for i in A.D[0]:
        for j in B.D[1]:
            sum = 0
            for k in A.D[1]:
                sum += getitem(A,(i,k))*getitem(B,(k,j))
            result.f[(i,j)] = sum
    return result
################################################################################

class Mat:
    def __init__(self, labels, function):
        self.D = labels
        self.f = function

    __getitem__ = getitem
    __setitem__ = setitem
    transpose = transpose

    def __neg__(self):
        return (-1)*self

    def __mul__(self,other):
        if Mat == type(other):
            return matrix_matrix_mul(self,other)
        elif Vec == type(other):
            return matrix_vector_mul(self,other)
        else:
            return scalar_mul(self,other)
            #this will only be used if other is scalar (or not-supported). mat and vec both have __mul__ implemented

    def __rmul__(self, other):
        if Vec == type(other):
            return vector_matrix_mul(other, self)
        else:  # Assume scalar
            return scalar_mul(self, other)

    __add__ = add

    def __sub__(a,b):
        return a+(-b)

    __eq__ = equal

    def copy(self):
        return Mat(self.D, self.f.copy())

    def __str__(M, rows=None, cols=None):
        "string representation for print()"
        if rows == None:
            try:
                rows = sorted(M.D[0])
            except TypeError:
                rows = sorted(M.D[0], key=hash)
        if cols == None:
            try:
                cols = sorted(M.D[1])
            except TypeError:
                cols = sorted(M.D[1], key=hash)
        separator = ' | '
        numdec = 3
        pre = 1+max([len(str(r)) for r in rows])
        colw = {col:(1+max([len(str(col))] + [len('{0:.{1}G}'.format(M[row,col],numdec)) if isinstance(M[row,col], int) or isinstance(M[row,col], float) else len(str(M[row,col])) for row in rows])) for col in cols}
        s1 = ' '*(1+ pre + len(separator))
        s2 = ''.join(['{0:>{1}}'.format(c,colw[c]) for c in cols])
        s3 = ' '*(pre+len(separator)) + '-'*(sum(list(colw.values())) + 1)
        s4 = ''.join(['{0:>{1}} {2}'.format(r, pre,separator)+''.join(['{0:>{1}.{2}G}'.format(M[r,c],colw[c],numdec) if isinstance(M[r,c], int) or isinstance(M[r,c], float) else '{0:>{1}}'.format(M[r,c], colw[c]) for c in cols])+'\n' for r in rows])
        return '\n' + s1 + s2 + '\n' + s3 + '\n' + s4

    def pp(self, rows, cols):
        print(self.__str__(rows, cols))

    def __repr__(self):
        "evaluatable representation"
        return "Mat(" + str(self.D) +", " + str(self.f) + ")"
