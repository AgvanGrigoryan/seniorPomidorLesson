from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from store.models import Book
from store.serializers import BooksSerializer


class BooksApiTestCase(APITestCase):
    def test_get(self):
        # создаем временные экземпляры моделей для теста
        book_1 = Book.objects.create(name="test book 1", price=25)
        book_2 = Book.objects.create(name="test book 2", price=45)

        # с помощью функции reverse создаем полную ссылку для обращения к api, параметр передаем из url-ов дописывая '-list' если это список
        url = reverse('book-list')
        # получает данные по api запросу с помощью обращения к client.get() функции
        response = self.client.get(url)

        # собирает сериалайзер по тестовым моделям книг и возвращает data
        serializer_data = BooksSerializer([book_1, book_2], many=True).data

        # проверяет статус запроса к api на успешность(HTTP_200_OK)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

        # сравнивает данные полученные по обращению к api с данными сериалайзера
        self.assertEqual(serializer_data, response.data)
