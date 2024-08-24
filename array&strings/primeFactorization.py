def sumOfPrimeFactors(num):
  totalSum = 0
  orignialNum = num

  # Check for number of 2s that divide num
  while num % 2 == 0:
    totalSum += 2
    num //= 2

  # Check for odd factors from 3 onwards
  factor = 3 
  while factor * factor <= num:
    while num % factor == 0:
      totalSum += factor
      num //= factor
    factor += 2
  
  # If num is a prime number greater than 2
  if num > 2:
    totalSum += num
  
  return totalSum