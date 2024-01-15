def fibonacchi_list(n):
  fibonacchi_number = [0,1]
  for i in range(2, n+1):
    new_el = fibonacchi_number[i-1] + fibonacchi_number[i-2]
    fibonacchi_number.append(new_el)
  return  fibonacchi_number

inp = input('enter a number ')
number = int(inp)
if number > 1:
  print(fibonacchi_list(number))
if number == 1:
  print([0, 1])
elif number <= 0:
  print('Please, write a positive integer, greater than zero (0)')
