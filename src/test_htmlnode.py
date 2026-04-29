import unittest

from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_multiple_props_to_html(self):
        node = HTMLNode(tag="div", props={"class": "container", "id": "main"})
        actual = node.props_to_html()
        expected = ' class="container" id="main"'
        self.assertEqual(actual, expected)
    
    def test_no_props_to_html(self):
        node = HTMLNode(tag="div")
        actual = node.props_to_html()
        expected = ""
        self.assertEqual(actual, expected)

    def test_repr(self):
        node = HTMLNode(tag="div", props={"class": "container", "id": "main"})
        actual = repr(node)
        expected = "HTMLNode(tag=div, value=None, children=None, props={'class': 'container', 'id': 'main'})"
        self.assertEqual(actual, expected)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_p_with_props(self):
        node = LeafNode("p", "Hello, world!", props={"class": "container", "id": "main"})
        self.assertEqual(node.to_html(), '<p class="container" id="main">Hello, world!</p>')
    
    def test_leaf_to_html_p_with_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_leaf_to_html_raw_text(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
        

if __name__ == "__main__":
    unittest.main()