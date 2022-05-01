var Calc = require('./calc');
var calc = new Calc();
calc.emit('stop');
console.log(Calc.title + '接收到stop监听事件')