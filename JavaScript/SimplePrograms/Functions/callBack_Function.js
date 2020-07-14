// A function expression is when a function is assigned to a variable.
// function expression catSays
var catSays = function (max) {
  var catMessage = "";
  for (var i = 0; i < max; i++) {
    catMessage += "meow ";
  }
  return catMessage;
};

// function declaration helloCat accepting a callback
function helloCat(callbackFunc) {
  return "Hello " + callbackFunc(3);
}

// A function that is passed into another function is called a callback.
// pass in catSays as a callback function
console.log(helloCat(catSays) + "!!"); // Output: Hello meow meow meow !!
