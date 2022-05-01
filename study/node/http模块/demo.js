//加载http模块
var http = require('http');

console.log('请打开浏览器，输入地址:localhost:520/')
//创建http服务器//监听网站时回环地址 端口520
http.createServer(function(req,res){
    res.end('hello,nodejs!');
    console.log('服务器正常!');
}).listen(520,'127.0.0.1');
