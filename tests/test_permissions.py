from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from api.models import CustomUser
from books.models import Book

class BookPermissionsTests(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='testpassword', role='user')
        self.admin_user = get_user_model().objects.create_user(username='adminuser', password='testpassword', role='admin')
        self.book = Book.objects.create(title='Test Book')

    def test_mark_book_viewed_as_user(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('mark-book-viewed', kwargs={'book_id': self.book.id})
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_mark_book_viewed_as_admin(self):
        self.client.force_authenticate(user=self.admin_user)
        url = reverse('mark-book-viewed', kwargs={'book_id': self.book.id})
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
