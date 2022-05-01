const string = 'abc';
const number = 1;
const boolean = true;
console.log(process.argv);
console.time('全部时间');
console.log(string,number,boolean);
console.time('计时');
for (var i = 0;i < 100000; i++) {}
console.timeEnd('计时');
console.timeEnd('全部时间');