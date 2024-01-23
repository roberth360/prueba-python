def palindromo(text):
 
  cad_min = text.lower().replace(" ", "")

  return cad_min == "".join(reversed(cad_min))

text = "oro"

print(palindromo(text))
