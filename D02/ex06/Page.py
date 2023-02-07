#!/usr/bin/python3

from elem import *
from elements import *

class Page:
    """
    Page will verify and write our html code.
    """
    def __init__(self, tree_path, element: Elem):
        self.page = element
        self.tree_path = tree_path
    
    def __str__(self) -> str:
        pass

    # def is_valid(self):
    #     """
    #     In this code, are there enough items?
    #     """
    #     is_enough = False
        
    #     #send if valid return True
    #     #send else return False
    
    def write_to_file(self, name):
        file_html = open({name} + ".html", "w")
        file_html.write(self.tree_path)
        file_html.close()

def main():
    html= Html([Head([Title(Text('"Hello ground!"'))]), \
        Body([H1(Text('"Oh no, not again!"')), \
            Img(attr={'src' : 'http://i.imgur.com/pfp3T.jpg'})])]) 

    Page(html, Elem)
    Page.write_to_file(Page, "test")
    # print(html)
    print(type(html))

if __name__ == '__main__':
    main()