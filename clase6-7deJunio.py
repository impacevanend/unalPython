"""
Librerias:
Numpy(arreglos en varias dimensiones), 
pandas,

"""

import numpy as np

# a = np.zeros((2,3,4))

# print(a.shape)
# print(a)

# print("--------")

# def log_entero(num, base=2):
#     cont = 0
#     while num >= base:
#         cont+=1
#         num /= base
#     return cont
# print(log_entero(1024))
# print(log_entero(1000,10))
# print(log_entero(9,3))


def variable_argument(var1, *vari):
    print("salida:"+ str(var1))
    for var in vari:
        print(var)
variable_argument(60)
variable_argument(100, 90, 67, 23, 10)