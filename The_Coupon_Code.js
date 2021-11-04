/*
Story
Your online store likes to give out coupons for special occasions. Some customers try to cheat the system by entering invalid codes or using expired coupons.

Task
Your mission:
Write a function called checkCoupon which verifies that a coupon code is valid and not expired.

A coupon is no more valid on the day AFTER the expiration date. All dates will be passed as strings in this format: "MONTH DATE, YEAR".

Examples:
checkCoupon("123", "123", "July 9, 2015", "July 9, 2015")  ===  true
checkCoupon("123", "123", "July 9, 2015", "July 2, 2015")  ===  false
*/

function checkCoupon(enteredCode, correctCode, currentDate, expirationDate){
  monthList = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];

  if (enteredCode == correctCode) {
    currentDate = currentDate.split(' ');
    expirationDate = expirationDate.split(' ');

    console.log(currentDate[2]);
    console.log(expirationDate[2]);
    if ((Number(currentDate[2]) <= Number(expirationDate[2]))) {
      console.log(monthList.indexOf(currentDate[0]));
      console.log(monthList.indexOf(expirationDate[0]));
      if (monthList.indexOf(currentDate[0]) < monthList.indexOf(expirationDate[0])) {
        return true;
      }
      else if (monthList.indexOf(currentDate[0]) == monthList.indexOf(expirationDate[0])) {
        if (Number(currentDate[1].replace(',', '')) <= Number(expirationDate[1].replace(',', ''))) {
          return true;
        }
      }
    }
  }
  return false;
}

// Testing
console.log(checkCoupon("123", "123", "July 9, 2015", "July 9, 2015")); //true
//console.log(checkCoupon("123", "123", "July 9, 2015", "July 2, 2015")); //false
//console.log(checkCoupon('123','123','September 5, 2014','October 1, 2014')) //true
//console.log(checkCoupon('123a','123','September 5, 2014','October 1, 2014')) //false
