/* Loop through the numbers 1 to 30
If the number is divisible by 3, print "Fizz" - "Garima"
If the number is divisible by 5, print "Buzz" - "Tuli"
If the number is divisible by both 3 and 5, print "FizzBuzz" - "GarimaTuli"
If the number is not divisible by 3 or 5, print the number
*/

// program of my own version of FizzBuzz called "GarimaTuli"

var FizzBuzz = function (n) {
  for (let i = 1; i <= n; i++) {
    let result =
      i % 3 === 0 && i % 5 === 0
        ? "GarimaTuli"
        : i % 3 === 0
        ? "Garima"
        : i % 5 === 0
        ? "Tuli"
        : i;
    console.log(i + " : " + result);
  }
};

FizzBuzz(30);
