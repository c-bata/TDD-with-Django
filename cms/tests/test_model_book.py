from django.test import TestCase
from cms.models import Book


class BookModelTests(TestCase):

    def test_is_empty(self):
        saved_books = Book.objects.all()
        self.assertEqual(saved_books.count(), 0)


