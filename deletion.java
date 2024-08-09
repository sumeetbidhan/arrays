// Starting at the index 1, we shift each element one position to the left
for (int i = 1; i < length; i++){
  // Shift each element one position to the left
  int_array[i - 1] = int_array[i];
}

length --;

// Say we want to delete the element at index 1
for (int i = 2; i < length; i++){
  // Shift each element one positio to the left
  int_array[i - 1] = int_array[i];
}

// The length needs to be consisitent with the current 
length --;
