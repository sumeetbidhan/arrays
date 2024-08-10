# 1. Initialize 
v0 = [] # equivalent to 'List<Integer> v0 = new ArrayList<>();'
v1 = None # equivalent to 'List<Integer> v1;' (v1 == null)

# 2. Cast an array to a list
a = [0, 1, 2, 3, 4] # equivalent to 'Integer[] a = {0, 1, 2, 3, 4};'
v1 = list(a) # Equivalent to  'v1 = new ArrayList <>(Arrays.asList(a));'

# 3. Make a copy 
v2 = v1 # another reference to v1
v3 = v1.copy() # Make an actual copy of v1

# 4. Get Length
print(f"The size of v1 is: {len(v1)}")

# 5. Access element
print(f"The first element in v1 is: {v1[0]}")

# 6. Iterate the list
print("[Version 1] The contents of v1 are:", end="")
for i in range(len(v1)):
    print(f" {v1[i]}", end="")
print()

print("[Version 2] The contents of v1 are:", end="")
for item in v1:
    print(f" {item}", end="")
print()

# 7. Modify element
v2[0] = 5  # Modifying v2 will actually modify v1
print(f"The first element in v1 is: {v1[0]}")

v3[0] = -1  # Modifying v3 will not affect v1
print(f"The first element in v1 is: {v1[0]}")

# 8. Sort
v1.sort()

# 9. Add new element at the end of the list
v1.append(-1)
v1.insert(1, 6)
v1.insert(2, 7)
print(v1)
# 10. Delete the last element
v1.pop()

# Final output to check the modifications
print("The final contents of v1 are:", v1)