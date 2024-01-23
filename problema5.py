def fibonacci(limite):
  
  a, b = 0, 1

  lista_fibonacci = []
  
  lista_fibonacci.append(a)
  lista_fibonacci.append(b)
  
  for i in range(2, limite + 1):
    
    nuevo_numero = a + b

    lista_fibonacci.append(nuevo_numero)
    a = b
    b = nuevo_numero

  return lista_fibonacci

limite = int(input("Ingrese el número límite: "))

lista_fibonacci = fibonacci(limite)

print("Los primeros Fibonacci hasta {} son:".format(limite))
for numero in lista_fibonacci:
  print(numero)
  
