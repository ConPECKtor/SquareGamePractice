

def factorial(n):
  if n <= 0:
      raise ValueError("Без отрицательных чисел!!!")
  result = 1
  for i in range(1, n + 1):
      result *= i
  return result
