import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
	def test_eq(self):
		node = TextNode("This is a text node", TextType.BOLD)
		node2 = TextNode("This is a text node", TextType.BOLD)
		self.assertEqual(node, node2)
	
	def test_not_eq(self):
		not_eq_node = TextNode("This is a text node", TextType.ITALIC)
		not_eq_node2 = TextNode("This is a different text node", TextType.ITALIC)
		self.assertNotEqual(not_eq_node, not_eq_node2)

	def test_text_type_eq(self):
		text_type_node = TextNode("This is a text node", TextType.BOLD)
		text_type_node2 = TextNode("This is a text node", TextType.ITALIC)
		self.assertNotEqual(text_type_node, text_type_node2)

	def test_url(self):
		url_node = TextNode("This is a url test node", TextType.BOLD, "www.google.com")
		no_url_node = TextNode("This is a url test node", TextType.BOLD)
		self.assertNotEqual(url_node, no_url_node)

if __name__ == "__main__":
	unittest.main()
