var dict = new Map();
dict.set('a', 1);
dict.set('e', 2);
dict.set('i', 3);
dict.set('o', 4);
dict.set('u', 5);

function encode(string) {
  string = string.split('')
  for (var i = 0; i < string.length; i++) {
    if (dict.has(string[i])) {
      string[i] = dict.get(string[i]);
    }
  }
  return string.join('');
}

function decode(string) {
  string = string.split('');
  for (var i = 0; i < string.length; i++) {
    dict.forEach((value, key) => {
      if (value == string[i]) {
        string[i] = key;
      }
    })
  }
  return string.join('');
}


// Testing
console.log(encode("hello"));
console.log(decode("h2ll4"));

// Restlt: Success
// Optimal Solution
/*
function encode(string){
  var vowelMapping = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5};
  return codeStringGivenMapping(string, vowelMapping);
}

function decode(string){
  var vowelMapping = {'1': 'a', '2': 'e', '3': 'i', '4': 'o', '5': 'u'};
  return codeStringGivenMapping(string, vowelMapping);
}

function codeStringGivenMapping(string, mapping){
  return string.split('').map(function(char){
    return mapping[char] || char;
  }).join('');
}
*/
