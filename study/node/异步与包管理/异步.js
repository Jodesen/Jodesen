//异步模式
console.log('小王开始服务');
//送餐服务
function service(){
    //setTimeout代码执行时，不会阻塞后面的代码执行
    setTimeout(function (){
        console.log('小王为A送餐');
    },0);
    setTimeout(function (){
        console.log('小王为B送餐');
    },0);
    setTimeout(function (){
        console.log('小王为C送餐');
    },0);
}
service();
console.log('A下单。');
console.log('B下单。');
console.log('C下单。');

