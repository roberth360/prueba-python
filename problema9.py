def num_par(list_num):
  
  list_num_par = []

  for num in list_num:
    if num % 2 == 0:
      list_num_par.append(num)

  return list_num_par



list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(num_par(list_num)) 
