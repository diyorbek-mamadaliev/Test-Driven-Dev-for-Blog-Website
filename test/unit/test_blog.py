from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog("Test Title", "Author")

        self.assertEqual("Test Title", b.title)
        self.assertEqual("Author", b.author)
        self.assertListEqual([], b.posts)
        # self.assertEqual(len([]), len(b.posts))

    def test_repr(self):
        b = Blog("Test", "Author")
        b2 = Blog("My Day", "John")

        self.assertEqual(b.__repr__(), "Test by Author (0 posts)")
        self.assertEqual(b2.__repr__(), "My Day by John (0 posts)")

    def test_repr_multiple(self):
        b = Blog("Test", "Author")
        b.posts = ["test"]

        b2 = Blog("My Day", "John")
        b2.posts = ["test", "another"]

        self.assertEqual(b.__repr__(), "Test by Author (1 post)")
        self.assertEqual(b2.__repr__(), "My Day by John (2 posts)")

