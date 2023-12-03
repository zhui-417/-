def main():
    print(
        '****欢迎使用图书管理系统***\n'
        '****     请选择        ***\n'
        '****1.借书       2.还书***\n'
        '****3.添加图书 4.删除图书**\n'
        '****5.查询所有图书*********\n'
     )
    s=input("请选择：")
    if s =='1':
        lend_book()
    elif s=='2':
        return_book()
    elif s=='3':
        add_book()
    elif s=='4':
        dele_book()
        exit()

from lend import lend_book
from return0 import return_book
from adds import add_book
from dels import dele_book



    
    


    
   
    
    