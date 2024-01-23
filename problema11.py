fact = lambda numero: numero * fact(numero - 1) if numero > 0 else 1


print(fact(5))
