def xor(a,b):
    return ['0' if a[i] == b[i] else '1' for i in range(len(a))]
def set_bit(i, N):
    return (1 << i) & N
def subset(A, ans):
    for v in range(2**len(A)):
        result = '0000000' 
        for i in range(len(ans)):
            if set_bit(i, v):
                result = xor(result, A[i])
        if result == [i for i in ans]:
            print v
A=['1110000','0111000','0011100','0001110','0000111','0000011']
subset(A, '0100010')
subset(A, '0010010')               
