from rest_framework import viewsets

from api import models
from api import serializers


class WebsiteViewSet(viewsets.ModelViewSet):
    queryset = models.Website.objects.all().select_related('category')
    serializer_class = serializers.WebsiteSerializer
