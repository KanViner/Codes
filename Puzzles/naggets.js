// Можно ли разложить count наггетсов по коробкам вмещающим 20, 9 и 6 штук?
// Коробок бесконечное колличество, но нельза наполнять коробку не до конца.
// Например нельзя положить в "20 коробу" лишь 17 наггетсов.
// Не обязательно использовать коробки всех номиналов.
// Например на count=40 функция вернет true, так как 40 = 20 + 20

const BASKETS = [20, 9, 6];

function isNuggetly(count) {
  for (basket of BASKETS) {
    if (basket === count) {
      return true;
    } else if (basket < count) {
      if (isNuggetly(count - basket)) {
        return true;
      }
    }
  }
  return false;
}

console.log(isNuggetly(44)); // true
console.log(isNuggetly(73)); // true
console.log(isNuggetly(100)); // true
console.log(isNuggetly(150)); // true
console.log(isNuggetly(1)); // false
console.log(isNuggetly(13)); // false
console.log(isNuggetly(31)); // false
console.log(isNuggetly(43)); // false
