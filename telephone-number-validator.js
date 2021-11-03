function telephoneCheck(str) {
  let testRegExp = new RegExp(
    /^(1\s?)?((\(\d{3}\))|(\d{3}))(-?|\s?)(\d{3})((?<=\-\d{3}\-)|-|\s?)(\d{4})$/g
  );
  let res = testRegExp.test(str);
  return res;
}
