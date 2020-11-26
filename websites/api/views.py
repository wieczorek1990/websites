from django_filters import rest_framework
from rest_framework import generics
from rest_framework import viewsets

from api import models
from api import serializers


class WebsiteViewSet(viewsets.ModelViewSet):
    queryset = models.Website.objects.all().select_related('category')
    serializer_class = serializers.WebsiteSerializer


class QueryWebsiteView(generics.ListAPIView):
    queryset = models.Website.objects.all()
    serializer_class = serializers.WebsiteSerializer
    filter_backends = [rest_framework.DjangoFilterBackend]
    filterset_fields = ['category']
