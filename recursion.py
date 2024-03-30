def fib(n):
  if n in [1, 2]:
    return 1
  else:
    return fib(n-1)+fib(n-2)

inp = input('enter a number ')
number = int(inp)
if number > 0:
  print([fib(number) for number in range(1,number+1)])
else:
  print('Please, write a positive integer, greater than zero (0)')