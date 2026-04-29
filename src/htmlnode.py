class HTMLNode:
    def __init__(self, tag: str = None, value: str = None, children: list["HTMLNode"]  = None, props: dict[str, str] = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html is not implemented")

    def props_to_html(self):
        if not self.props:
            return ""
        formatted_props = []
        for key, value in self.props.items():
            formatted_props.append(f" {key}=\"{value}\"")
        return "".join(formatted_props)
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict[str, str] = None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Value is required for leaf nodes")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list["HTMLNode"], props: dict[str, str] = None):
        super().__init__(tag=tag, children=children, props=props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag is required for parent nodes")
        if self.children is None:
            raise ValueError("Children are required for parent nodes")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
        
       
    
