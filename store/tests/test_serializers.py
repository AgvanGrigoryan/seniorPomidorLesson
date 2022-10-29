from django.test import TestCase

from store.models import Book
from store.serializers import BooksSerializer


class BooksSerializerTestCase(TestCase):
    def test_ok(self):
        # создаем временные экземпляры моделей для теста
        book_1 = Book.objects.create(name="serializer test book 1", price=7845)
        book_2 = Book.objects.create(name="serializer test book 2", price=8956)

        serializer_data = BooksSerializer([book_1, book_2], many=True).data
        excepted_data = [
            {
                'id': book_1.id,
                'name': 'serializer test book 1',
                'price': '7845.00'
            },
            {
                'id': book_2.id,
                'name': 'serializer test book 2',
                'price': '8956.00'
            }
        ]
        self.assertEqual(excepted_data, serializer_data)
