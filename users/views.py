from django.contrib.auth.models import User
from rest_framework import filters, generics, permissions
from django_filters.rest_framework import DjangoFilterBackend

from .permissions import IsSelfOrAdmin
from .serializers import UserSerializer


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = [
        'username',
        'email',
        'is_active',
    ]

    search_fields = [
        'username',
        'email',
        'first_name',
        'last_name',
    ]

    ordering_fields = [
        'id',
        'username',
        'email',
        'date_joined',
    ]

    ordering = ['id']

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.AllowAny()]

        return [permissions.IsAuthenticated()]


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsSelfOrAdmin,
    ]