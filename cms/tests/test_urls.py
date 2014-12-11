from django.core.urlresolvers import resolve
from django.test import TestCase
from cms.views import book_list, book_edit, book_del


class UrlResolveTests(TestCase):
    def test_url_resolves_to_book_list_view(self):
        """/cms/book/では、book_listが呼び出される事を検証"""
        found = resolve('/cms/book/')
        self.assertEqual(found.func, book_list)

    def test_url_resolves_to_book_add_view(self):
        """/cms/book/add/では、book_editが呼び出される事を検証"""
        found = resolve('/cms/book/add/')
        self.assertEqual(found.func, book_edit)

    def test_url_resolves_to_book_mod_view(self):
        """/cms/book/mod/では、book_editが呼び出される事を検証"""
        found = resolve('/cms/book/mod/1/')
        self.assertEqual(found.func, book_edit)

    def test_url_resolves_to_book_del_view(self):
        """/cms/book/del/では、book_delが呼び出される事を検証"""
        found = resolve('/cms/book/del/1/')
        self.assertEqual(found.func, book_del)