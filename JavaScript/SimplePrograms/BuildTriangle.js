// Build Triangle

// creates a line of * for a given length
function makeLine(length) {
  var line = "";
  for (var j = 1; j <= length; j++) {
    line += "* ";
  }
  return line + "\n";
}

// build triangle by calling makeLine()
function buildTriangle(length) {
  // building a huge string equivalent to the triangle
  var triangle = "";

  //start from the topmost line
  var lineNumber = 1;

  for (lineNumber = 1; lineNumber <= length; lineNumber++) {
    // not printing one line at a time.
    // Rather, making a huge string that will comprise the whole triangle
    triangle = triangle + makeLine(lineNumber);
  }
  return triangle;
}

// function buildTriangle() returns a string
// because the console.log() accepts a string argument
console.log(buildTriangle(10));
