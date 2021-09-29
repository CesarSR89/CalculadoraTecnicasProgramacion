#Debe realizar una aplicación en el lenguaje de su preferencia, que realice las siguientes funciones (40%):
#i. Suma.
#ii. Resta.
#iii. Multiplicación.
#iv. División.
#v. Verificación de número primo.
#vi. Verificación de número palíndromo.

print('\n         + - * / Calculadora(Funciones Basicas Matemáticas) / * - + \n')

def numeroPrimo(numeroIngresado):
    if numeroIngresado < 2:
        print("El numero",numeroIngresado,"no es primo")
        return False
    for divisor in range(2, numeroIngresado):
        if numeroIngresado % divisor == 0:
            print("El numero",numeroIngresado,"no es primo")
            return False
    print("El numero",numeroIngresado,"es primo")
    return True

print(" Ingrese los números que desea utilizar para aplicar las operaciones Matemáticas basicas \n")

primerNumero = int(input("Digite un numero: "))
segundoNumero = int(input("Digite otro numero: "))

opcion = 0
while opcion != 7:
    print("\nMENÜ\n","1.Suma Numeriaca\n","2.Resta Numeriaca\n","3.Multiplicacion Numeriaca\n",
          "4.Division Numeriaca\n","5.Verificación de número primo\n",
          "6.Verificación de número palíndromo\n","7.Salir")
    
    opcion = int(input("\nElija una opción: "))

    if opcion == 1:
        suma = primerNumero + segundoNumero
        print("Se ingresaron los numeros:",primerNumero,"y",segundoNumero,". La suma entre ellos es:",suma)

    elif opcion == 2:
        resta = primerNumero - segundoNumero
        print("Se ingresaron los numeros:",primerNumero,"y",segundoNumero,". La resta entre ellos es:",resta)

    elif opcion == 3:
        multiplicacion = primerNumero * segundoNumero
        print("Se ingresaron los numeros:",primerNumero,"y",segundoNumero,". La multiplicacion entre ellos es:",multiplicacion)

    elif opcion == 4:
        division = primerNumero / segundoNumero
        print("Se ingresaron los numeros:",primerNumero,"y",segundoNumero,". La division entre ellos es:",round(division,2))
        
    elif opcion == 5:
        numeroParaValidar = int(input("\nDigite un numero: "))

        numeroPrimo(numeroParaValidar)
        
    elif opcion == 6:
        numeroDigitado = input("\nDigite un numero: ").lower()
        numeroInvertido = numeroDigitado[::-1] #Se usa para optener la forma inversa de una lista o cadena #https://es.stackoverflow.com/questions/217819/que-es-1-en-python
        if numeroDigitado == numeroInvertido:
            print("El numero",numeroDigitado,"es palindromo")
        else:
            print("El numero",numeroDigitado,"no es palindromo")

    elif opcion == 7:
        print("Salió del sistema")

    else:
        print('Dato ingresado desconocido')
