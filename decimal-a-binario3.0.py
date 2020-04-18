# Programa para convertir de decimal a binario y luego a la norma de IEEE-754


def binario(numerito, lugares = 3):
    s = 0
    numerito_int, numerito_float = numerito.split(".")
    numerito_int = int(numerito_int)
    if (numerito_int < 0):
        s = 1
        numerito_int *=  -1
    numerito_float = int(numerito_float)
    # res = bin(numerito_int).lstrip("0b") + "." 
    res_temp = entero(numerito_int)
    res = reverse_slicing(res_temp) + "."

    for i in range (lugares): #aqui truena cuando la funcion regresa 0
        try:
            numerito_int, numerito_float = str((decimal(numerito_float)) * 2).split(".")
        except:
            return s,res

        numerito_float = int(numerito_float)
        res += numerito_int
    
    return s,res
    
    
def decimal(numerito):
    while numerito > 1:
        numerito /= 10
    return numerito


def entero(n):
    binario_int = ""
    while (n >= 1 and n != 0):
        binario_int += str(n%2)
        n = (n//2)
    
    return binario_int


def reverse_slicing(s):
    return s[::-1] 


def listToString(l):
    string = ""
    for i in l:
        string += i
    return string


def redondeo(e,M,n):
    M = list(M)
    lo_que_llevo = 0
    if M[n] == "0":
        M = M[1:n]
    
    elif M[n + 1] == "1" and M[n + 2] == "1" or M[n + 1] == "1" and M[n + 2] == "0":
        for i in range (n, 1, -1):
            if M[i] == "1" and lo_que_llevo == 0:
                lo_que_llevo = 1
                M[i] = "0"

            elif M[i] == "0" and lo_que_llevo == 1:
                M[i] = "1"
                lo_que_llevo = 0

        if lo_que_llevo == 1:
            e +=1
            lo_que_llevo = 0
    
    M = listToString(M)
    return e,M


def IEEE(m, s, e, n): 
    aux, aux_2 = m.split(".")
    if (aux == "0"):
        for i in range (0,len(aux_2)):
            if aux_2[i] == '1':
                e -=  i
    else:
        e += len(aux) - 1
    M = aux[0] + '.' + aux[1:] + aux_2
    # print (len(M))
    if (len(M) > n):
        e, M = redondeo(e,M,n)
    e = entero(e)
    e = reverse_slicing(e)
    return s, e, M



if __name__ == "__main__":
    e = 127
    m = ""
    n = input("introduce el numerito: ")
    # n = "78952.26545"

    p = (input("Presicion simple o doble? (s/d)"))
    # p = 'd'

    if (p == 's'):
        s, m = binario(n, lugares = 24)
        n = 24
        if (s == 0):
            print(m)
        else:
            print('-',m)

    elif (p == 'd'):
        s, m = binario(n, lugares = 53)
        n = 53
        if (s == 0):
            print(m)
        else:
            print('-',m)
    else:
        print("mala letra")

    print (IEEE(m,s,e,n))
    