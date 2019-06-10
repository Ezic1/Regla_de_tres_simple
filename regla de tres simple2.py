                # tercer intento de regla de tres simple 
                # compleramente funcional pero en vez de , es necesario usar .
print('bienvenidos a el programa de regla de tres simple v. 3000 xd ') 
print('en este programa para indicar numeros con decimales se lo debera indicar con "." si no dara error... gracias')    
print('a ----------> b')
print('c-----------> x = b * c / a')
mientras = 'si' # Esta variable es la que mantiene el bucle funcionando, si se cambia su valor el bucle terminara 
while mientras == 'si': 
    print('Dime el valor de a:')
    a = input()
    print('Dime el valor de b:')
    b = input()
    print('Dime el valor de c:')
    c = input()
    a = float(a) #estas tres funciones cambian el tipo de variable a float (numeros con decimales)
    b = float(b)
    c = float(c)
    x = b * c / a
    x = str(x) #esto cambia el valor del resultado a str (texto) para que no de error al usar la funcion print
    print('su resultado es: ' + x)
    print('Desea continuar? si para continuar.')
    mientras = input() 