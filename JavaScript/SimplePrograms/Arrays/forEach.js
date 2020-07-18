/* Use the array's forEach() method to loop over an array
 * and add 100 to each of the values if the value is divisible by 3 */

var test = [1, 2, 3, 5, 6, 7, 9, 24, 37];
console.log(test);

var x = test.forEach((item, index) => {
  if (item % 3 === 0)
    // The commented statements below would not be able to change the value of item
    // because the `item` is a COPY of actual element, while actual is test[index]
    //   item = item + 100;
    //   console.log(item); // temporary copy changes
    //   console.log(test[index]); // No effect on actual array
    test[index] = test[index] + 100;
});
//console.log(x); //forEach always returns undefined
console.log(test); // [ 1, 2, 103, 5, 106, 7, 109, 124, 37 ]
