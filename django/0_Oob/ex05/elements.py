from elem import Elem, Text

class Html(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__(tag = 'html', attr=attr, content=content, tag_type='double')

class Head(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__(tag = 'head', attr=attr, content=content, tag_type='double')

class Body(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__(tag = 'body', attr=attr, content=content, tag_type='double')

class Title(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__(tag = 'title', attr=attr, content=content, tag_type='double')

class Meta(Elem):
    def __init__(self, attr=None):
        super().__init__(tag = 'meta', attr=attr, content=None, tag_type='simple')

class Img(Elem):
    def __init__(self, attr=None):
        super().__init__(tag = 'img', attr=attr, content=None, tag_type='simple')

class Table(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__(tag = 'table', attr=attr, content=content, tag_type='double')

class Th(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__(tag = 'th', attr=attr, content=content, tag_type='double')

class Tr(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__(tag = 'tr', attr=attr, content=content, tag_type='double')

class Td(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__(tag = 'td', attr=attr, content=content, tag_type='double')

class Ul(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__(tag = 'ul', attr=attr, content=content, tag_type='double')

class Ol(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__(tag = 'ol', attr=attr, content=content, tag_type='double')

class Li(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__(tag = 'li', attr=attr, content=content, tag_type='double')

class H1(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__(tag = 'h1', attr=attr, content=content, tag_type='double')

class H2(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__(tag = 'h2', attr=attr, content=content, tag_type='double')

class P(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__(tag = 'p', attr=attr, content=content, tag_type='double')

class Div(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__(tag = 'div', attr=attr, content=content, tag_type='double')

class Span(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__(tag = 'span', attr=attr, content=content, tag_type='double')

class Hr(Elem):
    def __init__(self, attr=None):
        super().__init__(tag = 'hr', attr=attr, content=None, tag_type='simple')

class Br(Elem):
    def __init__(self, attr=None):
        super().__init__(tag = 'br', attr=attr, content=None, tag_type='simple')

if __name__ == "__main__":
    html1 = Html([Head(), Body()])
    print(html1)

    print("\n---\n")

    html2 = Html([Head(Title(Text('"Hello ground!"'))), Body([H1(Text('"Oh no, not again!"')), Img({"src" : "http://i.imgur.com/pfp3T.jpg"})])])
    print(html2)

    print("\n---\n")

    html3 = Html([
                Head([
                    Title(Text('"Hello ground!"')),
                    Meta({"charset" : "utf-8"}),
                    Meta({"name" : "author", "content" : "danjimen"})
                ]),
                Body([
                    H1(Text('This is the title h1')),
                    Div([
                        H2(Text("This is the h2 sub-title")),
                        P([
                            Text("This is a fake text with a "),
                            Span(Text("span text"), {"style" : "color:blue"}),
                            Text(" within the"),
                            Br(),
                            Text("paragraph itself.")
                        ])
                    ], {"style" : "background-color:red"}),
                    H2(Text("Table Test:")),
                    Table([
                        Tr([
                            Th(Text("Days")),
                            Th(Text("Weather"))
                        ], {"style" : "border: 1px solid blue; border-collapse: collapse"}),
                        Tr([
                            Td(Text("Monday")),
                            Td(Text("Sunny"))
                        ], {"style" : "border: 1px solid blue; border-collapse: collapse"}),
                        Tr([
                            Td(Text("Tuesday")),
                            Td(Text("Rainy"))
                        ], {"style" : "border: 1px solid blue; border-collapse: collapse"})
                    ], {"style" : "border: 1px solid blue; border-collapse: collapse"}),
                    Div([
                        H2(Text("Unordened lists"), {"style" : "text-decoration:underline"}),
                        Ul([
                            Li(Text("First element")),
                            Li(Text("Second element")),
                            Li(Text("Last element"))
                        ]),
                        Hr(),
                        H2(Text("Ordened lists"), {"style" : "text-decoration:underline"}),
                        Ol([
                            Li(Text("First element")),
                            Li(Text("Second element")),
                            Li(Text("Last element"))
                        ])
                    ], {"style" : "background-color:violet"}),
                    Img({"src" : "http://i.imgur.com/pfp3T.jpg"})
                ])
            ])
    print(html3)