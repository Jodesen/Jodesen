var util = require('util');
var EventEmitter = require('events').EventEmitter;
var Calc = function(){
    var self = this;
    this.on('stop',function (){
        console.log('触发计算器stop监听事件');
    });
};
util.inherits(Calc,EventEmitter);
Calc.prototype.add = function (a,b){
    return a+b;
}
module.exports = Calc;
module.exports.title = '计算器'