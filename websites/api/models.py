from django.db import models


class WebsiteCategory(models.Model):
    name = models.TextField()
    description = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    # count = models.IntegerField(default=0)  # TODO(lwieczorek): Find out what it's about


class Website(models.Model):
    url = models.CharField(max_length=2048)
    title = models.TextField()
    meta_description = models.TextField()
    alexa_rank = models.IntegerField()
    category = models.ForeignKey(WebsiteCategory, models.CASCADE)
    date_added = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)


class WebPage(models.Model):
    website = models.ForeignKey(Website, models.CASCADE)
    url = models.CharField(max_length=2048)
    date_added = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    title = models.TextField()
    meta_description = models.TextField()
