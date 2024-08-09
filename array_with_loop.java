int[] squareNumbers = new int[10];

// Go through each of the Array indexes, from 0 to 9.
for (int i=0; i < 10; i ++){
  int square = (i + 1) * (i + 1);
  squareNumbers[i] = square;
}

// More elegnat way of writing the code

for (int square : squareNumbers){
  // print the current value of square.
  System.out.println(square);
}