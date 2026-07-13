from rest_framework import status
from rest_framework.test import APITestCase

from .models import UserProfile


class UserProfileAPITestCase(APITestCase):

    def setUp(self):
        self.user_profile = UserProfile.objects.create(
            name='Tarun Saxena',
            email='tarun@gmail.com',
            phone='9876543210',
            city='Agra'
        )

    def test_create_user_profile(self):
        data = {
            'name': 'Rahul Sharma',
            'email': 'rahul@gmail.com',
            'phone': '9876500000',
            'city': 'Delhi'
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

    def test_list_user_profiles(self):
        response = self.client.get('/api/users/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_get_single_user_profile(self):
        response = self.client.get(
            f'/api/users/{self.user_profile.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_user_profile(self):
        data = {
            'city': 'Noida'
        }

        response = self.client.patch(
            f'/api/users/{self.user_profile.id}/',
            data,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_user_profile(self):
        response = self.client.delete(
            f'/api/users/{self.user_profile.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )