from wenjian import open_wj
from main import main
def add_book():
    print('欢迎添加图书')
    a_name=input('请输入书本名称')
    a_isdn=input('请输入isdn编号')
    word_1=a_name
    word_2=a_isdn
    open_wj(r"C:\Users\14498\Desktop\python\canlend.txt",word_1)
    open_wj(r'C:\Users\14498\Desktop\python\bookisdn.txt',word_2)
    print(
        '*************\n'
        '**1.继续添加**\n'
        '**2.退出添加**\n'
        '*************\n'
    )
    s=input('choose:')
    if s=="1":
        add_book()
    elif s=="2":
        main()

