#!/usr/bin/python3


class Text(str):
    """
    A Text class to represent a text you could use with your HTML elements.

    Because directly using str class was too mainstream.
    """

    def __str__(self):
        """
        Do you really need a comment to understand this method?..
        """
        # Escapamos primero los caracteres y luego aplicamos el salto de línea <br />
        content =  super().__str__().replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')
        return content.replace('\n', '\n<br />\n')
        # [...]


class Elem:
    """
    Elem will permit us to represent our HTML elements.
    """
    # [...]
    class ValidationError(Exception):
        pass

    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        """
        __init__() method.

        Obviously.
        """
        # [...]
        self.tag = tag
        self.attr = attr if attr is not None else {}
        self.tag_type = tag_type
        # self.content = content

        # Validar y formatear el contenido inicial
        if content is not None and not self.check_type(content):
            raise self.ValidationError
        
        if content is None:
            self.content = []
        elif isinstance(content, list):
            self.content = [c for c in content if c != Text('')]
        else:
            self.content = [content] if content != Text('') else []

    def __str__(self):
        """
        The __str__() method will permit us to make a plain HTML representation
        of our elements.
        Make sure it renders everything (tag, attributes, embedded
        elements...).
        """
        attr = self.__make_attr()
        result = "<{tag}{attr}".format(tag=self.tag, attr=attr)
        if self.tag_type == 'double':
            # [...]
            result += ">{content}</{tag}>".format(content=self.__make_content(), tag=self.tag)
        elif self.tag_type == 'simple':
            # [...]
            result += " />"
        return result

    def __make_attr(self):
        """
        Here is a function to render our elements attributes.
        """
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        """
        Here is a method to render the content, including embedded elements.
        """

        if len(self.content) == 0:
            return ''
        result = ''
        for elem in self.content:
            # Convertimos el elemento a string
            content_str = str(elem)
            # Para cada línea del contenido, le añadimos 2 espacios de sangría
            formatted_lines = content_str.replace('\n', '\n  ')
            result += f"\n  {formatted_lines}"
            # result += [...]
        return result + '\n'

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if type(content) == list:
            self.content += [elem for elem in content if elem != Text('')]
        elif content != Text(''):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        """
        Is this object a HTML-compatible Text instance or a Elem, or even a
        list of both?
        """
        return (isinstance(content, Elem) or type(content) == Text or
                (type(content) == list and all([type(elem) == Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))


if __name__ == '__main__':
    # [...]
    html = Elem('html', content=[
        Elem('head', content=Elem('title', content=Text('"Hello ground!"'))),
        Elem('body', content=[
            Elem('h1', content=Text('"Oh no, not again!"')),
            Elem('img', attr={'src': 'http://i.imgur.com/pfp3T.jpg'}, tag_type='simple')
        ])
    ])
    print(html)
