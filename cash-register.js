function checkCashRegister(price, cash, cid) {
  let currencyLookup = {
    PENNY: 0.01,
    NICKEL: 0.05,
    DIME: 0.1,
    QUARTER: 0.25,
    ONE: 1.0,
    FIVE: 5.0,
    TEN: 10.0,
    TWENTY: 20.0,
    "ONE HUNDRED": 100.0,
  };
  let res = { status: "", change: [] };
  let totalCID = cid.reduce((sum, cur) => sum + cur[1], 0).toFixed(2);
  let totalChange = (cash - price).toFixed(2);
  if (parseFloat(totalCID) < parseFloat(totalChange)) {
    res.status = "INSUFFICIENT_FUNDS";
    res.change = [];
  } else if (totalCID === totalChange) {
    res.status = "CLOSED";
    res.change = cid;
  } else {
    res.status = "OPEN";
    for (let i = cid.length - 1; i >= 0; --i) {
      let cur = cid[i][0],
        amt = cid[i][1].toFixed(2),
        val = currencyLookup[cid[i][0]].toFixed(2);
      while (
        parseFloat(amt).toFixed(2) - parseFloat(val).toFixed(2) >= 0 &&
        parseFloat(totalChange).toFixed(2) - parseFloat(val).toFixed(2) >= 0
      ) {
        amt -= val;
        totalChange -= val;
        let found = false;
        for (let i = 0; i < res.change.length; ++i) {
          if (res.change[i][0] === cur) {
            found = true;
            let sum = parseFloat(res.change[i][1]) + parseFloat(val);
            res.change[i][1] = sum;
          }
        }
        if (!found) {
          res.change.push([cur, parseFloat(val)]);
        }
      }
    }
    if (parseFloat(totalChange).toFixed(2) > 0) {
      res.status = "INSUFFICIENT_FUNDS";
      res.change = [];
    }
  }
  return res;
}
