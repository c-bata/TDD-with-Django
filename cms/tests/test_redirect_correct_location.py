from unittest import skip
from django.http import HttpRequest
from django.test import TestCase
from cms.views import book_edit, book_del


class RedirectCorrectLocation(TestCase):
    @skip
    def test_book_add_redirects_after_post(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['name'] = 'name'

        response = book_edit(request)
        self.assertEqual(response['location'], '/cms/book/')

    @skip
    def test_book_del_redirects_after_post(self):
        request = HttpRequest()
        response = book_del(request)
        self.assertEqual(response['location'], '/cms/book/')
