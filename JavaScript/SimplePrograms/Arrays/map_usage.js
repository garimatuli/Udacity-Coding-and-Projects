/* Use the map() method to take the array of bill amounts
 * and create a second array of numbers called totals that shows
 * the bill amounts with a 15% tip added */

var bills = [50.23, 19.12, 34.01, 100.11, 12.15, 100.1, 6.77, 2.22];

var totals = bills.map((bill) => {
  bill = bill + 0.15 * bill;
  return Number(bill.toFixed(2));
});

console.log(totals);

// toFixed() to round numbers to 2 decimal places.
// toFixed() returns string
// Number(str) to convert string str to a Number
