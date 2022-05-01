//加载module.js模块文件
// var moudle = require('./module.js');
//使用模块
console.log('abs(-273) = %d',moudle.abs(-273));
console.log('circleArea(3) = %d',moudle.circleArea(3));

var Hello = require('./module.js');
hello = new Hello();
hello.setName('jodesen')
hello.sayHello();