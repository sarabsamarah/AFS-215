const Instance = require('./Class')

const test1 = new Instance(3)
const test2 = new Instance(6)
const test3 = new Instance(7)
const test4 = new Instance(14)
const test5 = new Instance(21)
const stringify = new Instance(10)
const testWord = new Instance("Hi!")


console.log(test1.display(test1))
console.log(test2.display(test2))
console.log(test3.display(test3))
console.log(test4.display(test4))
console.log(test5.display(test5))
console.log(stringify.display(stringify))
console.log(testWord.display(testWord))
