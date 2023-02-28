# Escribe un programa calculadora que reciba como parámetros dos enteros (num1 y num2) desde su llamada y que los
# muestre por pantalla. A continuación, se deberá solicitar al usuario que seleccione la operación matemática a
# realizar entre los dos números. Las operaciones que implementará serán suma, resta, multiplicación, división
# y potencia.

entero1 = int(input('Escribe un número entero.'))
entero2 = int(input('Escribe otro número entero.'))
print('')

print(f" Numero entero 1 = {entero1}. \n"
      f" Numero entero 2 = {entero2}. \n")

print(f" Elige la operación a realizar: \n + \n - \n * \n / \n ** (potencia)")

simbolo = input('¿Operación?')

if simbolo == '+':
    print(f"{entero1} {simbolo} {entero2} = {entero1 + entero2}")

if simbolo == '-':
    print(f"{entero1} {simbolo} {entero2} = {entero1 - entero2}")

if simbolo == '*':
    print(f"{entero1} {simbolo} {entero2} = {entero1 * entero2}")

if simbolo == '/':
    if entero2 == 0:
        print('No se puede dividir entre 0.')
    else:
        print(f"{entero1} {simbolo} {entero2} = {round(entero1 / entero2, 2)}")

if simbolo == '**':
    print(f"{entero1} {simbolo} {entero2} = {entero1 ** entero2}")
