from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase


class UserAPITestCase(APITestCase):
    def setUp(self):
        self.admin = User.objects.create_superuser(
            username='admin',
            email='admin@gmail.com',
            password='admin123'
        )

        self.user = User.objects.create_user(
            username='tarun',
            email='tarun@gmail.com',
            password='tarun123'
        )

    def test_create_user(self):
        data = {
            'username': 'rahul',
            'email': 'rahul@gmail.com',
            'password': 'rahul123'
        }

        response = self.client.post(
            '/api/users/',
            data,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_list_users(self):
        self.client.force_authenticate(user=self.admin)

        response = self.client.get('/api/users/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_user_can_update_own_profile(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.patch(
            f'/api/users/{self.user.id}/',
            {'first_name': 'Tarun'},
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_user_cannot_update_other_user(self):
        second_user = User.objects.create_user(
            username='second',
            password='second123'
        )

        self.client.force_authenticate(user=self.user)

        response = self.client.patch(
            f'/api/users/{second_user.id}/',
            {'first_name': 'Wrong Update'},
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )