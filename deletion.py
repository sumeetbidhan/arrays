# Initialize an integer array with some elements
int_array = [1, 2, 3, 4, 5]
length = len(int_array)

# Starting at index 1, shift each element one position to the left
for i in range(1, length):
  # Shift each element one position to the left
  int_array[i - 1] = int_array[i]

# Decrease the lenght
length -= 1

print(int_array)

# Remove the last element since it's now duplicated
int_array.pop()
print(int_array)