
#* carácter. Al conjunto de caracteres usadoscon este fin se le llama Esquema de codificacion. 


"""
Esquema de codificación cuyo objetivo es dar a cada carácter usado por
cada uno de los lenguajes humanos su propio código,

Python usa ASCII


\n : Una nueva l ́ınea
\t : Una tabulaci ́on
\" : Una comilla doble
\’ : Una comilla simple
\\ : El car ́acter de diagonal invertida (backslash)
\u0105 : El car ́acter
\u01F4 : El car ́acter G ́


Se usan los operadores convencionales (<, <=, >, >=, ==, !=) para
comparar cadenas usando el orden lexicogr ́afico.

todo funciones:
la funci ́on len() determina la longitud de una cadena. Para el programa

La funci ́on slice() obtiene una porci ́on (subcadena) de una cadena. La
notaci ́on es similar a la funci ́on range, [inicio:fin:incremento]. Para
el programa

El m ́etodo count() obtiene las veces que una subcadena se encuentra en
una cadena (o en una parte de ella). La notaci ́on es
count(subcadena, inicio, fin). Para el programa


Los m ́etodos find() y rfind() obtienen la primera y  ́ultima ocurrencia de una
subcadena en una cadena (o en una parte de ella), respectivamente. La
notaci ́on es find/rfind(subcadena, inicio, fin). Para el programa


print(s.lower()) # Muestra la cadena en min ́usculas
print(s.upper()) # Muestra la cadena en may ́usculas
print(s.capitalize()) # Primer letra a may ́uscula
print(s.title()) # Primer letra cada palabra a may ́uscula
print(s.swapcase()) # May ́usculas <-> min ́usculas


El m ́etodo strip/lstrip/rstrip remueve los caracteres deseados a los
dos lados/izquierda/derecha de una cadena. La notaci ́on es
strip/lstrip/rstrip(caracteres). Si no se dan caracteres como
argumento, elimina espacios en blanco (espacios y tabulaciones).


El m ́etodo split() divide una cadena de acuerdo a una subcadena que sirve
como delimitador, dejando las partes separadas en una lista. La notaci ́on
es split(delimitador). Para el programa


Existen cuatro m ́etodos para justificar cadenas:
ljust() : Justificar una cadena a la izquierda
rjust() : Justificar una cadena a la derecha
center() : Centrar una cadena
zfill() : Llenar una cadena con ceros


El m ́etodo replace reemplazar una subcadena en una cadena por otra. la
notaci ́on es replace(anterior, nueva).


endswith : Determinar si una cadena termina con.
startswith : Determinar si una cadena empieza con.
isalpha : Determinar si una cadena contiene letras  ́unicamente.
isalnum : Determinar si una cadena contiene n ́umeros y letras
 ́unicamente (alfanum ́erico).
isdigit : Determinar si una cadena contiene s ́olo d ́ıgitos.
isspace : Determinar si una cadena contiene s ́olo espacios.
istitle : Determinar si una cadena es un t ́ıtulo.
islower : Determinar si una cadena contiene todos sus caracteres en
min ́usculas.
isupper : Determinar si una cadena contiene todos sus caracteres en
may ́uscula.

"""