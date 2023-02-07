#!/usr/bin/python3

from elem import *

class Html(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('html', attr=attr, content=content)

class Head(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('head', attr=attr, content=content)

class Body(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('body', attr=attr, content=content)

class Title(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('title', attr=attr, content=content)

class Meta(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('meta', attr=attr, content=content, tag_type='simple')

class Img(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('img', attr=attr, content=content, tag_type='simple')

class Table(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('table', attr=attr, content=content)

class Th(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('th', attr=attr, content=content)

class Tr(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('tr', attr=attr, content=content)

class Td(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('td', attr=attr, content=content)

class Ul(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('ul', attr=attr, content=content)

class Ol(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('ol', attr=attr, content=content)

class Li(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('li', attr=attr, content=content)

class H1(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('h1', attr=attr, content=content)

class H2(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('h2', attr=attr, content=content)

class P(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('p', attr=attr, content=content)

class Div(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('div', attr=attr, content=content)

class Br(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('br', attr=attr, content=content, tag_type='simple')

class Hr(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('hr', attr=attr, content=content, tag_type='simple')

class Span(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('span', attr=attr, content=content)

def function_tester():
    # First test (format html)
    # print(Html([\
    #     Head([\
    #         Title(), (Meta())\
    #             ]), \
    #     Body([\
    #          H1(), Br(), P(), H2(), Div(), Img(), Span(), Hr(), Table([\
    #             Tr([Th(), Th(), Th()]), Tr([Td(), Td(), Td()]), Tr([Td(), Td(), Td()])\
    #                 ]), Ul([Li(), Li()]), Ol([Li(), Li()]), \
    #             ])\
    #         ] ) )

    # Second test (each of the classes)
    # classes = [Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br]
    # for elem in classes:
    #     print(elem())

    # Third test (pdf test)
    print(Html([\
    Head([\
        Title(Text('"Hello ground!"'))\
            ]), \
    Body([\
            H1(Text('"Oh no, not again!"')), Img(attr={'src' : 'http://i.imgur.com/pfp3T.jpg'}) \
            ])\
        ] ) )


if __name__ == '__main__':
    function_tester()