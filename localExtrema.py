def numLocalExtrema(arr):
  length = len(arr)
  if length < 5:
    return 0 # As per constraints, length should be >= 5
  
  count = 0

  for i in range(1, length - 1):
    if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
      count += 1
    elif arr[i] < arr[i - 1] and arr[i] < arr[ i + 1]:
      count += 1
  
  return count 
