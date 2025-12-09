# open(file,mode,buffering,encoding,errors)，一般用open函数传参时对encoding="UTF-8"用关键字传参

#读取文件  f.read(n)读取n个字节
#读取文件  f.readLines(n) 注意前面的读取会对后面的产生影响，只能继续接着前面的读
# f.read()时读取全部内容 lines = f.readlines() 读取文件全部行，封装到列表中，会读取换行符
#for 循环读取文件行 for line in f
#文件的关闭 f.close()
#with open() as f: 会在对调用文件操作完后自动关闭
f = open("D:/新建文本文档.txt",'r',encoding="utf-8")
# 统计a的数量
# i = 0
# for line in f:
#     count = line.count("a")
#     i += count
# print(i)

g = open("D:/新建文本文档(结果).txt",'w',encoding="utf-8")
for line in f:
    if line.count("a") == 0:
        g.write(line)
f.close()
g.close()

