#primeNumbers.py

import time


def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True
  1
x = int(input("how many prime numbers do you want to calculate: "))
i = 0
while i<x:
  i=i+1
  if is_prime(i)==True:
    print(str(i) + " is a prime number")
    time.sleep(1)
  #else:
    #print(str(i) + " is not a prime number")
    #time.sleep(1)