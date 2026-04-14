print("hello world")

from textnode import TextNode, TextType

def main():
    text_nodes = [
        TextNode("Hello, world!", TextType.PLAIN_TEXT),
        TextNode("**Bold text**", TextType.BOLD_TEXT),
        TextNode("_Italic text_", TextType.ITALIC_TEXT),
        TextNode("`Code text`", TextType.CODE_TEXT),
        TextNode("[anchor text](url)", TextType.LINK, "https://www.boot.dev"),
        TextNode("![alt text](url)", TextType.IMAGE, "https://www.boot.dev"),
    ]

    print(text_nodes)

if __name__ == "__main__":
    main()