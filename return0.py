from wenjian import open_r1,open_wj,open_wf
from main import main
def return_book():
    isdn=open_r1(r'C:\Users\14498\Desktop\python\isdn.txt')
    namebook=open_r1(r'C:\Users\14498\Desktop\python\lended.txt')
    for i in range(0,len(isdn)):
        isdn[i]=isdn[i].rstrip("\n")
        namebook[i]=namebook[i].rstrip("\n")

        print(
            '***请选择还书方式***\n'
            '*******************\n'
            '***1.查找书名*******\n'
            '***2.查找书号*******\n'
            '*******************\n'
        )
        s=input('choose:')
        if s=="1":
            s==input("书籍名称：")
            for x in range(0,len(namebook)):
                if s==namebook[x]:
                    print("成功找到书本",namebook[x])
                    print('即将执行还书操作,确认后请按Y')
                    print('-----------------------信息')
                    print("书籍名称：",namebook[x])
                    print('书籍编号：',isdn[x])
                    s=input("请确认(Y/N)")
                    if s=="Y":
                        word_1=namebook[x]
                        word_2=isdn[x]
                        open_wj(r'C:\Users\14498\Desktop\python\canlend.txt',word_1)
                        open_wj(r'C:\Users\14498\Desktop\python\bookisdn.txt',word_2)
                        isdn.pop(x)
                        namebook.pop(x)
                        word1=isdn[0]
                        word2=namebook[0]
                        open_wf(r'C:\Users\14498\Desktop\python\lended.txt',word2)
                        open_wf(r'C:\Users\14498\Desktop\python\isdn.txt',word1)
                        for i in range(0,len(isdn)-1):
                            word_1=isdn[i+1]
                            word_2=namebook[i+1]
                            open_wj(r'C:\Users\14498\Desktop\python\isdn.txt',word_1)
                            open_wj(r'C:\Users\14498\Desktop\python\lended.txt',word_2)
                        print('书已经归还')
                        main()  
                    elif s=="N":
                        main()
                else:
                    if x==len(namebook)-1:
                        print('没有找到图书',s,'请检查拼写')
                        main()  
        elif s=='2':
            s=input("请输入编号")
            for x in range(0,len(isdn)):
                if s==isdn[x]:
                    print("成功找到书本",namebook[x])
                    print('即将执行还书操作,确认后请按Y')
                    print('-----------------------信息')
                    print("书籍名称：",namebook[x])
                    print('书籍编号：',isdn[x])
                    s=input("请确认(Y/N)")
                    if s=="Y":
                        word_1=namebook[x]
                        word_2=isdn[x]
                        open_wj(r'C:\Users\14498\Desktop\python\canlend.txt',word_1)
                        open_wj(r'C:\Users\14498\Desktop\python\bookisdn.txt',word_2)
                        isdn.pop(x)
                        namebook.pop(x)
                        word1=isdn[0]
                        word2=namebook[0]
                        open_wf(r'C:\Users\14498\Desktop\python\lended.txt',word2)
                        open_wf(r'C:\Users\14498\Desktop\python\isdn.txt',word1)
                        for i in range(0,len(isdn)-1):
                            word_1=isdn[i+1]
                            word_2=namebook[i+1]
                            open_wj(r'C:\Users\14498\Desktop\python\isdn.txt',word_1)
                            open_wj(r'C:\Users\14498\Desktop\python\lended.txt',word_2)
                        print('书已经归还')
                        main()  
                    elif s=="N":
                        main()
                else:
                    if x==len(namebook)-1:
                        print('没有找到图书',s,'请检查拼写')
                        main()  

                    



