from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser

from .models import Cat
from .permissions import IsAdminOrReadOnly, IsOwnerOrAdminOrReadOnly
from .serializers import CatSerializer


class CatAPIList(generics.ListCreateAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    authentication_classes = (TokenAuthentication,)
    lookup_field = 'slug'
    # pagination_class = CatAPIListPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(title__icontains=search_query)
        return queryset


class CatAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    # permission_classes = (IsOwnerOrAdminOrReadOnly, )
    authentication_classes = (TokenAuthentication, )
    lookup_field = 'slug'

class CatAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    permission_classes = (IsAdminUser, )
    authentication_classes = (TokenAuthentication,)
    lookup_field = 'slug'

class UserCatListView(generics.ListAPIView):
    serializer_class = CatSerializer

    def get_queryset(self):
        username = self.kwargs.get('username')
        return Cat.objects.filter(user__username=username, user=self.request.user)

