from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from store.models import Book
from store.serializers import BooksSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer


def books_list_page_view(request):
    return render(request, 'index.html', {'orders': Book.objects.all()})



