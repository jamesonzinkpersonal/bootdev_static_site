import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)
    
    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(repr(node), "TextNode(This is a text node, bold, None)")

    def test_text_type_not_equal(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.ITALIC_TEXT)
        self.assertNotEqual(node, node2)
    
    def test_url_not_equal(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT, "https://www.google.com")
        self.assertNotEqual(node, node2)
    
    def test_text(self):
        node = TextNode("This is a text node", TextType.PLAIN_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

if __name__ == "__main__":
    unittest.main()