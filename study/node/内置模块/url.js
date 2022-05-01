//使用url模块
var url = require('url');
var querystring = require('querystring');
//调用parse方法
var parseObject = url.parse('http://search.jd.com/Searcj?keyword=java&enc=utf-8&wq=java&pvid=425de9f31d014547807ff3ab31e81af1');
console.log(querystring.parse(parseObject.query));

