from django.http import HttpRequest
from cms.views import book_edit
from django.test import TestCase


class CanSaveAPostRequestAssert(TestCase):
    def assertFieldInResponse(self, response, name, page, publisher):
        self.assertIn(name, response.content.decode())
        self.assertIn(page, response.content.decode())
        self.assertIn(publisher, response.content.decode())


class CanSaveAPostRequestTests(CanSaveAPostRequestAssert):
    def post_request(self, name, page, publisher):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['name'] = name
        request.POST['page'] = page
        request.POST['publisher'] = publisher
        return request

    def test_book_edit_can_save_a_post_request(self):
        name, page, publisher = 'name', 'page', 'publisher'
        request = self.post_request(name, page, publisher)
        response = book_edit(request)
        self.assertFieldInResponse(response, name, page, publisher)
