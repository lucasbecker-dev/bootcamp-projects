function palindrome(str) {
  let testStr = [...str.toLowerCase()].filter((char) => /[a-z0-9]/i.test(char));
  for (let i = 0; i < Math.floor(testStr.length / 2); ++i) {
    if (testStr[i] !== testStr[testStr.length - 1 - i]) {
      return false;
    }
  }
  return true;
}
