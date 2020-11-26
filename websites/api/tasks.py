import csv
import urllib.request
import zipfile
from celery import shared_task

from api import models


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
        to_read = 10
        i = 0
        for row in reader:
            print(row)
            i += 1
            if i >= to_read:
                break
