def caracter_5(list_palabras):

  return [palabra for palabra in list_palabras if len(palabra) > 5]

list_palabras = ["car", "uno", "carros", "universidad", "xls"]

print(caracter_5(list_palabras))
