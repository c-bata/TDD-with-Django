from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
from cms.views import book_list, book_edit


class HtmlTests(TestCase):
    def test_book_list_page_returns_correct_html(self):
        request = HttpRequest()
        response = book_list(request)
        expected_html = render_to_string('cms/book_list.html',
                                         {'books': []})
        self.assertEqual(response.content.decode(), expected_html)

