// Declare an integer array of 6 elements
int [] intArray = new int[6];
int length = 0;

// Add 3 elements to the Array
for (int i = 0; i < 3; i++){
  intArray[length] = i;
  length++;
}

for (int i = 0; i < intArray.length; i++){
  System.out.println("Index" + i + "contains" + intArray[i]);
}

// Insert a new element at the end of the Array.
intArray[length] = 10;
length++;

// Inserting at the Start of an Array
// We do this by shifting each element one index to the right
for (int i = 3; i >= 0; i--){
  intArray[i + 1] = intArray[i];
}

intArray[0] = 20;
