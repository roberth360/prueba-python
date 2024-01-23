primo = lambda numero: numero > 1 and all(numero % i != 0 for i in range(2, int(numero ** 0.5) + 1))

numero = 11

print(primo(numero))
