# 1. Initialize
a0 = [0] * 5 # Equivalent to 'int[] a0 = new int[5];'
a1 = [1, 2, 3] # equivalent to 'int[] a1 = {1, 2, 3};'

# 2. Get Length 
print(f"The size of a1 is: {len(a1)}")

# 3. Access Element 
print(f"The first size element is: {a1[0]}")

# 4. Iterate all Elements
print("[Version 1] The contents of a1 are: ", end=" ")

for i in range(len(a1)):
  print(f"{a1[i]}", end=" ")
print()

print("[Version2] The contents of a1 are: ", end=" ")
for item in a1:
  print(f"{item}", end=" ")
print()

# 5. Modify Element
a1[0] = 4

# 6. Sort
a1.sort()

# Print the sorted array to check the result
print("The sorted contents of a1 are: ", a1)