# Loop from 0 to 4
for i in range(5):
  print(i)

colors = ['red', 'green', 'blue']

# Loop over list indices
for i in range(len(colors)):
  print(f"Index: {i}, Color: {colors[i]}")

# Nested loops: Multiplication Table
for i in range(1, 4):
  for j in range(1, 4):
    print(f"{i} X {j} = {i * j}")
  print() # Print a blank line after each row

# Nested loop: Pattern Printing
# Print a right angle triangle pattern
for i in range(1, 6):
  for i in range(0,i):
    print(f"*", end="")
  print()

print()

n = 5
for i in range(1, n + 1):
  for j in range(i):
    print('*', end='')
  print() # Move to the next line after each row

print()

# Using range with a Step Value
# Loop from 0 to 10 with a step of 2
for i in range(0, 11, 2):
  print(i)

print()
# Looping Backwards
# Loop backwards from 5 to 1
for i in range(5, 0, -1):
  print(i)
