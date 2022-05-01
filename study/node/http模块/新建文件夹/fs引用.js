//引用模块
const fs = require('fs');
fs.readFile('1.txt','utf8',function(erro,data){ //读取文件
    if(erro){
        return console.log('读取文件失败！'+erro.message);
    }
    console.log('读取文件成功'+data);
});
//调用fs.writeFile()方法，写入文件的内容
//  参数1以表示文件的存放路径
//  参数2表示要写入的内容
//  参数3回调函数
fs.writeFile('1.txt','abcdef',function(err){
    //文件写入成功着回调函数值为null
    console.log(err);

if(err){
    return console.log('文件写入失败' + err.message)
}
    console.log('文件写入成功！')
})