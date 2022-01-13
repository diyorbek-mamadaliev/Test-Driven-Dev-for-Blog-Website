from unittest import TestCase
from post import Post

class PostTest(TestCase):
    def test_create_post(self):
        p = Post("Test", "Post Content")

        self.assertEqual("Test", p.title)
        self.assertEqual("Post Content", p.content)

    def test_json(self):
        p = Post("Test", "Post Content")
        expected = {"title" : "Test", "content" : "Post Content"}

        self.assertDictEqual(expected, p.json())