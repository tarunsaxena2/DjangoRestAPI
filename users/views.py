from rest_framework import generics
from .models import UserProfile
from .serializers import UserProfileSerializer


class UserListCreateView(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all().order_by('id')
    serializer_class = UserProfileSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer