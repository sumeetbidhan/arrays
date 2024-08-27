# Looping through a list with len
fruits = ['apple', 'banana', 'cherry']
for i in range(len(fruits)):
  print(f"Fruit {i + 1} : {fruits[i]}")


# Nested Loop Example (Multiplication table)
for i in range(1, 6):
  for j in range(1, 6):
    print(f"{i} X {j} = {i * j}", end="\t")
    # end = "\t" ensures the products are printed in a tabular format
  print()

print()

# Using range with step 
# loop through numbers from 10 to 0, stepping by -2
for i in range(10, -1, -2):
  print(i)

print()
# Looping through a list of lists(2D list)
matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

for row in matrix:
  for element in row:
    print(element, end=" ")
  print()

# Example with 'continue' and 'break'
for i in range(10):
  if i % 2 != 0:
    continue # Skip odd numbers
  if i == 6:
    break # Stop the loop when i is 6
  print(i)