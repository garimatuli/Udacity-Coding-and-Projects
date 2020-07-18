/* Use the array's map() method to loop over an array
 * and add 100 to each of the values if the value is divisible by 3 */

var test = [1, 2, 3, 5, 6, 7, 9, 24, 37];
console.log(test);

var test = test.map((item) => {
  if (item % 3 === 0) item = item + 100;
  return item;
});

console.log(test); // [ 1, 2, 103, 5, 106, 7, 109, 124, 37 ]
