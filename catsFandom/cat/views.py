from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import Cat
from .permissions import IsAdminOrReadOnly, IsOwnerOrAdminOrReadOnly
from .serializers import CatSerializer


class CatAPIList(generics.ListCreateAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    permission_classes = (IsAuthenticated, )
    lookup_field = 'slug'
    # pagination_class = CatAPIListPagination


class CatAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    permission_classes = (IsOwnerOrAdminOrReadOnly, )
    # authentication_classes = (TokenAuthentication, )
    lookup_field = 'slug'

class CatAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    permission_classes = (IsOwnerOrAdminOrReadOnly, )
    lookup_field = 'slug'
