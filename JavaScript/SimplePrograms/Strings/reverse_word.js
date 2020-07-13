// Reverse a String

var reverse_word = function (str) {
  let rev = "";
  // loops over the chracters in reverse order
  for (let i = str.length - 1; i >= 0; i--) {
    // add charcters to the word
    // rev = rev.concat(str[i]);
    rev = rev + str[i];
  }
  return rev;
};

console.log(reverse_word("Hello..!!")); // Output: !!..olleH
console.log(reverse_word("Hello World..!!")); // Output: !!..dlroW olleH
