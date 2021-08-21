"""
suma(5) = 5+4+3+2+1+0
suma(4) = 4+3+2+1+0
suma(n) = n + suma(n-1)

"""

# def suma(n):
#     if n == 0:
#         return 0
#     else:
#         a = suma(n-1)
#         print(a)
#         return n + a
    
    
# print(suma(5))


# def suma_parcial(l,n):
#     if n == 0:
#         return 0
#     else:
#         return l[n-1]+ suma_parcial(l, n-1)
    
# def suma_lista(l):
#     return suma_parcial(l,len(l))


# print(suma_lista([1,2,3,4,5]))
    
    
# def str_ch_parcial(cadena, char, n):
    
#     if n == 0:
#         return False
#     else:
#         return(cadena[n-1] == char) or str_ch_parcial(cadena,char,n-1)
    
# def str_ch(cadena,char):
#     return str_ch_parcial(cadena, char, len(cadena))
    
    
# print(str_ch("Leonardo","L"))


# def misteriosa(n):
#     if n == 0:
#         return True
#     elif n == 1:
#         return False
#     else:
#        return misteriosa(n-2) 
   
# lista = [0,1,2,3,4,5,6,7,8]

# for i in lista:
#     a = misteriosa(i)
#     print(i,a)
        
        
# def g(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     else:
#         return g(n-3)
    
# lista = [0,1,2,3,4,5,6,7,8]

# for i in lista:
#     a = g(i)
#     print(i,a)


# def h(n, m):
#     if m == 0:
#         return n
#     else:
#         return h(n+1,m-1)
    
# lista = [(2,3),(8,5),(6,6)]

# for i in lista:
#     a = h(i[0],i[1])
#     print(i,a)


# def mult(n,m):
#     if m == 1:
#         return n
#     else:
#         return n + mult(n, m-1)
    
# lista = [(2,3),(8,5),(6,6)]

# for i in lista:
#     a = mult(i[0],i[1])
#     print(i,a)

# def pot(n,m):
#     if m == 0:
#         return 1
#     else:
#         return n * pot(n, m-1)
    
# lista = [(2,3),(8,5),(6,6)]

# for i in lista:
#     a = pot(i[0],i[1])
#     print(i,a)


# def deuda(n):
#     if n == 0:
#         return 1000000
#     else:
#         return  deuda(n-1) + deuda(n-1) * 0.05
    

# print(deuda(12))


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
    
print(fib(12))


    
        