// Creat a new array with a capacity of 6
int[] array = new int[6];

// Current length is 0, beacuse it has 0 elements.
int length = 0;

// Add 3 items into it
for (int i = 0; i < 3; i++){
  array[i] = i * i;
  length++;
 }

System.out.println("The Array has a capacity of" + array.length);
System.out.println("The Array has a lenght of " + length );
