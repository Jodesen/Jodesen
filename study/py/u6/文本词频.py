'''
jieba.lcut(s) 精确模式返回一个列表类型的分词结果
jieba.lcut(s,cut_all=Ture)  全模式,返回一个列表类型的分词结果   有冗余
jieba.lcut_for_search(s)    搜索引擎模式,返回一个列表类型的分词结果  有冗余
'''
def gettext():
    txt = open('1.txt','r').read()
    txt = txt.lower()
    for ch in '!"#$%&()*+.-./:;<=>?@[\\]^_ .{|}·~‘’':
        txt = txt.replace(ch,'')
    return txt

hamlettxt = gettext()
words = hamlettxt.split()
counts={}
for word in words:
    counts[word] = counts.get(word,0)+1
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word,count = items[i]
    print('{0:<10}{1:>5}'.format(word,count))