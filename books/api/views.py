from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import response

from api import serializers
from api import models


class BookViewSet(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookFullDetailSerializer

    def list(self, request):
        queryset = models.Book.objects.all()
        serializer = serializers.BookListSerializer(queryset, many=True)
        return response.Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = models.Book.objects.all()
        book = get_object_or_404(queryset, pk=pk)
        serializer = serializers.BookDetailSerializer(book)
        return response.Response(serializer.data)


class PublisherViewSet(viewsets.ModelViewSet):
    queryset = models.Publisher.objects.all()
    serializer_class = serializers.PublisherSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorDetailSerializer

    def list(self, request):
        queryset = models.Author.objects.all()
        serializer = serializers.AuthorListSerializer(queryset, many=True)
        return response.Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = models.Author.objects.all()
        author = get_object_or_404(queryset, pk=pk)
        serializer = serializers.AuthorDetailSerializer(author)
        return response.Response(serializer.data)