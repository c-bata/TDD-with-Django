from django.test import TestCase
from cms.models import Book, Impression


class ImpressionModelTests(TestCase):
    def create_impression(self, comment=None):
        book = Book()
        book.save()

        impression = Impression()
        impression.book = book
        if comment is not None:
            impression.comment = comment
        impression.save()

    def test_is_empty(self):
        saved_books = Impression.objects.all()
        self.assertEqual(saved_books.count(), 0)

    def test_is_not_empty(self):
        self.create_impression()
        saved_books = Impression.objects.all()
        self.assertEqual(saved_books.count(), 1)

    def test_impression_size_equals_book_size(self):
        self.create_impression()

        saved_books = Book.objects.all()
        saved_impressions = Impression.objects.all()

        self.assertEqual(saved_books.count(),
                         saved_impressions.count())

    def test_saving_and_retrieving_impression(self):
        comment = 'impression comment'
        self.create_impression(comment)
        saved_impressions = Impression.objects.all()
        impression = saved_impressions[0]

        self.assertEqual(impression.comment, comment)
