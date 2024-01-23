def sum_num(list_num):
 
  sum_pos = 0
  sum_neg = 0

  for num in list_num:
    if num >= 0:
      sum_pos += num
    else:
      sum_neg += num

  return sum_pos, sum_neg



list_num = [1, 2, 3, -4, -5, -6, 7, 8, 9, 10]

sum_pos, sum_neg = sum_num(list_num)

print(sum_pos)  
print(sum_neg) 
