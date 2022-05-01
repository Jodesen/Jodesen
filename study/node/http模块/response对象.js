//创建web服务器，并监听端口
require('http').createServer(function (request,response){
    //返回响应内容
    response.writeHead(200,{ 'Content-Type':'text/html'});
    response.end('<h1>Hello,Node.js</h1>');
}).listen(520,function (){
    console.log('服务器监听地址是localhost:520');
});