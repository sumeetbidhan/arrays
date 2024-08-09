# Declare an integer array of 6 elements
int_array = [None] * 6
length = 0

# Add 3 elements to the array
for i in range(3):
  int_array[length] = i
  length += 1

for i in range(len(int_array)):
  print(f"Index {i} contains {int_array[i]}")

# Insert a new element at the end of the array
int_array[length] = 10
length += 1

# Inserting at the start of the array
# Shift each element one index to the right
for i in range(3, -1, -1):
  int_array[i + 1] = int_array[i]

int_array[0] = 20

# Print the final array state
for i in range(len(int_array)):
  print(f"Index {i} contains {int_array[i]}")