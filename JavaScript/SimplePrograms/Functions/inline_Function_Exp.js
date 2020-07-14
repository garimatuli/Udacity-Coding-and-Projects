// emotions() function definition
function emotions(myString, myFunc) {
  console.log("I am " + myString + ", " + myFunc(2));
}

// Inline Function Expression
// Calling the emotions() function with two arguments
// Argument 1 - "happy" string
// Argument 2 - an inline function expression
emotions("happy", function (num) {
  var sound = "";
  for (var i = 0; i < num; i++) {
    sound = sound + "ha";
  }
  sound = sound + "!";
  return sound;
});

// Output: I am happy, haha!
