# Escribe un programa que pida un número por teclado y que cree un diccionario cuyas claves sean desde el
# número 1 hasta el número indicado, y los valores sean los cuadrados de las claves.

numeros = {}
valor = ""

while valor != "-1":
    valor = input("Escribe un número.")
    if valor != "-1":
        valor = int(valor)
        for numero in range(1, valor+1):
            if numero not in numeros:
                 numeros[numero] = numero**2
            else:
                numeros[numero] = numero**2

    print(numeros)
