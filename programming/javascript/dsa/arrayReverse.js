function reverseArr(input) {
  var ret = new Array;
  for(var i = input.length-1; i >= 0; i--) {
      ret.push(input[i]);
  }
  return ret;
}


var a = [3,5,7,8]
var b = reverseArr(a);

console.log(b); // Option 1
var reversed = [...a].reverse(); // Option 2
console.log(reversed)