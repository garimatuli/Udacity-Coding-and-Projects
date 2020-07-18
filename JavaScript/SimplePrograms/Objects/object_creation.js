/* Create a variable `umbrella`, it should be an object
 * `umbrella` object should have the `color` and `isOpen` property
 * `umbrella` object should have an `open()` method that toggles the value of `isOpen` property
 * `umbrella` object should have an `close()` method that toggles the value of `isOpen`
 */

var umbrella = {
  color: "pink",
  isOpen: false,
  open: function () {
    if (umbrella.isOpen === true) {
      return "The umbrella is already opened!";
    } else {
      umbrella.isOpen = true;
      return "Garima opens the umbrella!";
    }
  },
  close: function () {
    if (umbrella.isOpen === true) {
      umbrella.isOpen = false;
      return "Garima closes the umbrella!";
    } else return "The umbrella is already closed";
  },
};

console.log("Umbrella Open? -> " + umbrella.isOpen);
console.log(umbrella.open());
console.log("Umbrella Open? -> " + umbrella.isOpen);
console.log(umbrella.open());
console.log("Umbrella Open? -> " + umbrella.isOpen);
console.log(umbrella.close());
console.log("Umbrella Open? -> " + umbrella.isOpen);
console.log(umbrella.close());
console.log("Umbrella Open? -> " + umbrella.isOpen);
