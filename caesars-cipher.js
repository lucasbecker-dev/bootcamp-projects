function rot13(str) {
  let alphaArr = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
  ];
  let testArr = [...str];
  let resArr = [];
  for (let elem of testArr) {
    if (/[^A-Z]/.test(elem)) {
      resArr.push(elem);
      continue;
    }
    if (alphaArr.indexOf(elem) + 13 >= alphaArr.length) {
      resArr.push(alphaArr[13 - (alphaArr.length - alphaArr.indexOf(elem))]);
    } else {
      resArr.push(alphaArr[alphaArr.indexOf(elem) + 13]);
    }
  }
  return resArr.join("");
}
