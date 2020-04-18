import math as m

def binario(n):
    binario_int = ""
    while (n >= 1 and n != 0):
        binario_int += str(n%2)
        n = m.floor(n/2)
    
    return binario_int

def reverse_slicing(s):
    return s[::-1]
n = 40

b = binario(n)
print (reverse_slicing(b))
print (bin(n))
