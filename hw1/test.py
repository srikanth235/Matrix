def xor(a, b):
    return ''.join([('0' if a[i] == b[i] else '1') for i in range(len(a))])
def test(S, index, value):
    if index < 0:
        return False
    if S[index] == value:
        print index, S[index]
        return True
    test(S, index-1, value)
    if test(S, index-1, xor(value, S[index])):
                print index, S[index]
S=['1100000','0110000','0011000','0001100','0000110','0000011']
test(S,len(S)-1,'0010010')
print "\n"
test(S,len(S)-1,'0100010')
