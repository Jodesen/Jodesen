//引用ctypto
var crypto = require('crypto')
//生成hash.
var shasum = crypto.createHash('sha256')
shasum.update('crypto_hash');
var output = shasum.digest('hex');
//输出密码
console.log('crypto_hash:',output);