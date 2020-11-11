import os
import datetime

from django import test
from django.core.files import uploadedfile
from django.conf import settings

from api import models


class BookTestCase(test.TestCase):
    def setUp(self) -> None:
        publisher = models.Publisher(name='Wydawnictwo Literackie')
        publisher.save()
        self.publisher_pk = publisher.pk
        image_path = os.path.join(os.path.join(settings.BASE_DIR, 'samples'), 'lód.jpg')
        self.cover_image = uploadedfile.SimpleUploadedFile(
            name='test_image.jpg',
            content=open(image_path, 'rb').read(),
            content_type='image/jpeg')
        book = models.Book(title='Lód', publisher=publisher,
                           pages_num=1014, cover_image=self.cover_image)
        book.save()
        author = models.Author(firstname='Jacek',
                               lastname='Dukaj',
                               nickname='Rekursja',
                               birthdate=datetime.date(1974, 7, 30))
        author.save()
        self.author_pk = author.pk
        book.authors.add(author)
        author = models.Author(firstname='Łukasz',
                               lastname='Wieczorek',
                               nickname='Sobek',
                               birthdate=datetime.date(1990, 9, 9))
        author.save()
        book.authors.add(author)
        book.save()
        self.book_pk = book.pk


class BookViewSetTestCase(BookTestCase):
    def test_list(self):
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, 200)

    def test_retrieve(self):
        response = self.client.get('/books/{}/'.format(self.book_pk))
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        response = self.client.delete('/books/{}/'.format(self.book_pk))
        self.assertEqual(response.status_code, 204)

    def test_post(self):
        response = self.client.post('/books/',
                                    data={
                                        'title': 'Powrót z gwiazd',
                                        'publisher': self.publisher_pk,
                                        'pages_num': 201,
                                        'cover_image': None,
                                    },
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_put(self):
        response = self.client.put('/books/{}/'.format(self.book_pk),
                                   data={
                                       'title': 'Powrót z gwiazd 2',
                                       'publisher': self.publisher_pk,
                                       'pages_num': 202,
                                       'cover_image': None,
                                   },
                                   content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_patch(self):
        response = self.client.patch('/books/{}/'.format(self.book_pk),
                                     data={
                                         'pages_num': 203,
                                     },
                                     content_type='application/json')
        self.assertEqual(response.status_code, 200)


class PublisherViewSetTestCase(BookTestCase):
    def test_list(self):
        response = self.client.get('/publishers/')
        self.assertEqual(response.status_code, 200)

    def test_retrieve(self):
        response = self.client.get('/publishers/{}/'.format(self.publisher_pk))
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        response = self.client.delete('/publishers/{}/'.format(self.publisher_pk))
        self.assertEqual(response.status_code, 204)

    def test_post(self):
        response = self.client.post('/publishers/',
                                    data={
                                        'name': 'Wydawnictwo Świńskie',
                                    },
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_put(self):
        response = self.client.put('/publishers/{}/'.format(self.publisher_pk),
                                   data={
                                       'name': 'Wydawnictwo Świńskie',
                                   },
                                   content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_patch(self):
        response = self.client.patch('/publishers/{}/'.format(self.publisher_pk),
                                     data={
                                         'name': 'Wydawnictwo Świńskie',
                                     },
                                     content_type='application/json')
        self.assertEqual(response.status_code, 200)


class AuthorViewSetTestCase(BookTestCase):
    def test_list(self):
        response = self.client.get('/authors/')
        self.assertEqual(response.status_code, 200)

    def test_retrieve(self):
        response = self.client.get('/authors/{}/'.format(self.author_pk))
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        response = self.client.delete('/authors/{}/'.format(self.author_pk))
        self.assertEqual(response.status_code, 204)

    def test_post(self):
        response = self.client.post('/authors/',
                                    data={
                                        'firstname': 'Stanisław',
                                        'lastname': 'Lem',
                                        'nickname': 'Bajkopisarz',
                                        'birthdate': datetime.date(1921, 9, 12),
                                    },
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_put(self):
        response = self.client.put('/authors/{}/'.format(self.author_pk),
                                   data={
                                       'firstname': 'Stanisław',
                                       'lastname': 'Lem',
                                       'nickname': 'Bajkopisarz dumny',
                                       'birthdate': datetime.date(1921, 9, 12),
                                   },
                                   content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_patch(self):
        response = self.client.patch('/authors/{}/'.format(self.author_pk),
                                     data={
                                         'lastname': 'Lemuś',
                                     },
                                     content_type='application/json')
        self.assertEqual(response.status_code, 200)
