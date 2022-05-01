#Tempconvert.py     #单行注释用’#‘
'''这是
多行注释'''
CD=input('请输入需要转换的温度：')
if CD[-1] in ['F','f']:
	C = (eval(CD[0:-1]) -32 )/1.8
	print('转换后的温度是：{:.2f}C'.format(C))
elif CD[-1] in ['C','c']:
	F = 1.8*eval(CD[0:-1])+32
	print('转换后的温度是：{:.2f}F'.format(F))
else:
	print('您输入的格式错误')
	