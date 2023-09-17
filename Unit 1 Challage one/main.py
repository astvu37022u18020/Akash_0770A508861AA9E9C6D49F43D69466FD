n = int(input("Enter factorial of n value : "))

def factorial(n):
  return 1 if (n < 1) else n * factorial(n - 1)

if __name__ == '__main__':

  print(f'The Factorial of {n} is', factorial(n))
