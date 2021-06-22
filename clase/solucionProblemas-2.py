"""
def epsilon(): 
    xo=1
    xi=1
    
    while 1 + xi > 1.0:
        xo = xi
        xi /=2
    return xo

print(f"El valor de Epsilon es: {epsilon}()")

"""

def primo(n):
    es_primo = True
    for i in range(2,round(n/2)+1):
        if (n % i) == 0:
            es_primo = False
            break
    return es_primo

print(primo())