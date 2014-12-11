from django.test import TestCase
from cms.forms import BookForm
from cms.models import Book


class BookFormTests(TestCase):
    def test_valid(self):
        """正常な入力を行えばエラーにならないことを検証"""
        params = dict(name='書籍タイトル', publisher='出版社', page=0)
        book = Book()  # book_idの指定なし(追加時)
        form = BookForm(params, instance=book)
        self.assertTrue(form.is_valid())

    def test_either1(self):
        """何も入力しなければエラーになることを検証"""
        params = dict()
        book = Book()  # book_idの指定なし(追加時)
        form = BookForm(params, instance=book)
        self.assertFalse(form.is_valid())