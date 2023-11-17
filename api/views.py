from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from books.models import Book
from books.serializers import BookSerializer

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class MarkBookView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, book_id):
        try:
            book = Book.objects.get(id=book_id)
            book.viewed_by.add(request.user)
            return Response({'message': 'Книга отмечена просмотренной.'})
        except Book.DoesNotExist:
            return Response({'error': 'Книга не найдена.'})