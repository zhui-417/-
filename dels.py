from wenjian import open_r1
from main import main
def dele_book():
    print('真的要删除吗，好吧')
    b_name=input('请输入要删除书的名称')
    b_isdn=input('请输入要删除isdn编号')
    bookname_1=open_r1(r"C:\Users\14498\Desktop\python\canlend.txt")
    bookisdn_1=open_r1(r'C:\Users\14498\Desktop\python\bookisdn.txt')
    word_1=b_name
    word_2=b_isdn
    bookname_1.pop(word_1)
    bookisdn_1.pop(word_2)
    print('删除好了')
    main()



