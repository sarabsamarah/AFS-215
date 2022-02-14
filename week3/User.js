module.exports = class User {
    constructor(name = "Marty", age = 29, num1 = 3, num2 = 7) {
      this.num1 = num1;
      this.num2 = num2;
      this.name = name;
      this.age = age;
    }
  
    add() {
      console.log(this.num1 + this.num2);
    }
  
    sub() {
      console.log(this.num1 - this.num2);
    }
  
    mul() {
      console.log(this.num1 * this.num2);
    }
  
    div() {
      console.log(this.num1 / this.num2);
    }
  
    helloAge() {
      console.log(`Hey ${this.name} ! You are ${this.age} years young.`);
    }
  
    stringVal() {
      let val = String(this.num1) + String(this.num2);
      console.log(val);
    }
  };