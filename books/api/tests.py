import os
import datetime

from django import test
from django.core.files import uploadedfile
from django.conf import settings

from api import models


class BookTest(test.TestCase):
    def test_create_book(self):
        publisher = models.Publisher(name='Wydawnictwo Literackie')
        publisher.save()
        image_path = os.path.join(os.path.join(settings.BASE_DIR, 'samples'), 'lód.jpg')
        cover_image = uploadedfile.SimpleUploadedFile(
            name='test_image.jpg',
            content=open(image_path, 'rb').read(),
            content_type='image/jpeg')
        book = models.Book(title='Lód', publisher=publisher,
                           pages_num=1014, cover_image=cover_image)
        book.save()
        author = models.Author(firstname='Jacek',
                               lastname='Dukaj',
                               nickname='Rekursja',
                               birthdate=datetime.date(1974, 7, 30))
        author.save()
        book.authors.add(author)
        book.save()
