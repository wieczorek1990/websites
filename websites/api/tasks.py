import csv
import hashlib
import requests
import urllib.request
import zipfile
from base64 import urlsafe_b64encode
from bs4 import BeautifulSoup
from celery import shared_task
from django.conf import settings

try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode

from api import models


WEBSITES_TO_PARSE_COUNT = 4


def webshrinker_categories_v3(access_key, secret_key, url=b"", params={}):
    params['key'] = access_key

    request = "categories/v3/{}?{}".format(urlsafe_b64encode(url).decode('utf-8'), urlencode(params, True))
    request_to_sign = "{}:{}".format(secret_key, request).encode('utf-8')
    signed_request = hashlib.md5(request_to_sign).hexdigest()

    return "https://api.webshrinker.com/{}&hash={}".format(request, signed_request)


@shared_task
def update_websites():
    url = 'http://s3.amazonaws.com/alexa-static/top-1m.csv.zip'
    filehandle, _ = urllib.request.urlretrieve(url)
    zip_file_object = zipfile.ZipFile(filehandle, 'r')
    first_file = zip_file_object.namelist()[0]
    file = zip_file_object.open(first_file)
    with open('websites.csv', 'wb') as f:
        f.write(file.read())
    with open('websites.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        models.Website.objects.all().delete()
        models.WebsiteCategory.objects.all().delete()
        models.WebPage.objects.all().delete()
        i = 0
        for row in reader:
            alexa_rank, url = row
            update_website(alexa_rank, url)
            i += 1
            if i >= WEBSITES_TO_PARSE_COUNT:
                break


def update_website(alexa_rank, url):
    api_url = webshrinker_categories_v3(settings.WEBSHIRNKER_ACCESS_KEY,
                                        settings.WEBSHRINKER_SECRET_KEY,
                                        url.encode('utf-8'))
    response = requests.get(api_url)
    if response.status_code != 200:
        return
    data = response.json()
    try:
        category_data = data['data'][0]['categories'][0]
    except IndexError:
        return
    category, _ = models.WebsiteCategory.objects.get_or_create(
        name=category_data['id'],
        defaults={'description': category_data['label']}
    )
    title, meta_description = get_url_meta(url)
    website, _ = models.Website.objects.get_or_create(
        url=url,
        defaults={'title': title,
                  'meta_description': meta_description,
                  'alexa_rank': alexa_rank,
                  'category': category}
    )


def get_url_meta(url):
    url = 'https://' + url
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features='html.parser')
    title = soup.find('title')
    description = soup.find('meta', attrs={'name': 'description'})
    if title is None:
        title = ''
    else:
        title = title.contents[0]
    if description is None:
        description = ''
    else:
        description = description.get('content')
    return title, description
