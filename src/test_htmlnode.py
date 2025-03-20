import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_with_props(self):
        node = HTMLNode(props={"href": "https://example.com"})
        self.assertEqual(node.props_to_html(), ' href="https://example.com"')

        node = HTMLNode(
            props={"href": "https://example.com", "target": "_blank"})
        # Note: The order of props may vary, so we need to check for both possibilities
        result = node.props_to_html()
        self.assertTrue(
            result == ' href="https://example.com" target="_blank"' or
            result == ' target="_blank" href="https://example.com"'
        )

    def test_props_to_html_without_props(self):
        # Test with None props
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

        # Test with empty props
        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(), "")

    def test_constructor(self):
        node = HTMLNode("p", "hello", [], {"class": "text"})
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "hello")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {"class": "text"})

    def test_to_html_raises_error(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(),
                         "<div><span>child</span></div>")

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
