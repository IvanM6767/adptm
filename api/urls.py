from django.urls import path
from .views import BookListView, MarkBookView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:book_id>/mark-viewed/', MarkBookView.as_view(), name='mark-book-viewed'),
]