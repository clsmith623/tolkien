class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        html_string = ""
        if not self.props:
            return html_string
        for k, v in self.props.items():
            html_string = html_string + " " + k + '="' + v + '"'
        return html_string

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        if not self.tag:
            return self.value
        return ("<" + self.tag + self.props_to_html() + ">" + self.value + "</" + self.tag + ">")

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        child_text = ""
        if not self.tag:
            raise ValueError("expected HTML tag")
        if self.children is None:
            raise ValueError("expected children value")
        for child in self.children:
            child_text += child.to_html()
        return ("<" + self.tag + self.props_to_html() + ">" + child_text + "</" + self.tag + ">")
