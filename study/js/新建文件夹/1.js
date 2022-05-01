//计时开始
console.time('时间')
var output = 1 ;
for (var i = 1; i <= 10; i++){
	output *= i;
}
console.log('Result:',output);
//计时结束
console.timeEnd('时间')