from rest_framework import serializers

from api import models


class WebsiteSerializer(serializers.ModelSerializer):
    category__name = serializers.SerializerMethodField()

    def get_category__name(self, website):
        return website.category.name

    class Meta:
        model = models.Website
        fields = ('url', 'title', 'meta_description', 'alexa_rank',
                  'category__name', 'date_added', 'date_updated')
