/* The `numbers` variable is an array of arrays.
 * Use a nested `for` loop to cycle through `numbers`.
 * Convert each even number to the string "even"
 * Convert each odd number to the string "odd" */

var numbers = [
  [243, 12, 23, 12, 45],
  [34, 2, 1, 553, 23, 4, 55],
  [67, 56, 45, 553, 44, 55, 5],
  [12, 31, 55, 445],
  [4, 2, 3, 52, 13, 51, 44],
];

for (let row = 0; row < numbers.length; row++) {
  for (let col = 0; col < numbers[row].length; col++) {
    if (numbers[row][col] % 2 === 0) numbers[row][col] = "even";
    else numbers[row][col] = "odd";
  }
}

console.log(numbers);
