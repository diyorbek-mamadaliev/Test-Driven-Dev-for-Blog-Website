from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog

class AppTest(TestCase):

    def test_input_menu(self):
        with patch("builtins.input") as mocked_input:
            app.menu()
            mocked_input.assert_called_once_with(app.MENU_PROMT)

    def test_menu_print_blogs(self):
        with patch("app.print_blogs") as mocked_print_blogs:
            with patch("builtins.input", return_value = "q"):
                app.menu()
                mocked_print_blogs.assert_called_once_with()

    def test_printing_blogs(self):
        blog = Blog("Test", "Author")
        app.blogs = {"Test" : blog}
        with patch("builtins.print") as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_once_with("- Test by Author (0 posts)")

    def test_ask_to_create_blog(self):
        with patch("builtins.input") as mocked_input:
            mocked_input.side_effect = ("Test", "Author")
            app.ask_to_create_blog()

            self.assertIsNotNone(app.blogs.get("Test"))