array_len = [None] * 6

array_length = 0

for i in range(0, 3):
  array_len[i] = i * i
  array_length += 1


print(f"The array has a capacity of {len(array_len)}")
print(f"The array has length of {array_length}")