from django.test import TestCase
from cms.models import Book


class BookAssertion(TestCase):
    def assertBookModel(self, actual_book, name, page, publisher):
        self.assertEqual(actual_book.name, name)
        self.assertEqual(actual_book.page, page)
        self.assertEqual(actual_book.publisher, publisher)


class BookModelTests(BookAssertion):
    def creating_a_book_and_saving(self, name=None, page=None, publisher=None):
        book = Book()
        if name is not None:
            book.name = name
        if page is not None:
            book.page = page
        if publisher is not None:
            book.publisher = publisher
        book.save()

    def test_is_empty(self):
        saved_books = Book.objects.all()
        self.assertEqual(saved_books.count(), 0)

    def test_is_not_empty(self):
        self.creating_a_book_and_saving()
        saved_books = Book.objects.all()
        self.assertEqual(saved_books.count(), 1)

    def test_saving_and_retrieving_book(self):
        name, page, publisher = 'name', 10, 'publisher'
        self.creating_a_book_and_saving(name, page, publisher)

        saved_books = Book.objects.all()
        actual_book = saved_books[0]

        self.assertBookModel(actual_book, name, page, publisher)
