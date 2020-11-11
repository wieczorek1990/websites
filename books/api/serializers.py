from rest_framework import serializers

from api import models


class BookListSerializer(serializers.ModelSerializer):
    publisher_name = serializers.SerializerMethodField()

    def get_publisher_name(self, book):
        return book.publisher.name

    class Meta:
        model = models.Book
        fields = ('id', 'title', 'cover_image',
                  'publisher_name')


class BookDetailSerializer(BookListSerializer):
    author_names = serializers.SerializerMethodField()

    def get_author_names(self, book):
        names = ['{} {}'.format(author.firstname, author.lastname)
                 for author in book.authors.all()]
        return ', '.join(names)

    class Meta:
        model = models.Book
        fields = ('id', 'title', 'cover_image', 'pages_num',
                  'publisher_name', 'author_names')


class BookFullDetailSerializer(BookDetailSerializer):
    class Meta:
        model = models.Book
        fields = ('id', 'title', 'cover_image', 'pages_num', 'publisher',
                  'publisher_name', 'author_names')


class BookImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = ('id', 'cover_image')


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Publisher
        fields = ('id', 'name')


class AuthorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = ('id', 'firstname', 'lastname', 'nickname', 'birthdate')


class AuthorDetailSerializer(serializers.ModelSerializer):
    books_titles = serializers.SerializerMethodField()

    def get_books_titles(self, author):
        titles = [book.title for book in author.book_set.all()]
        return ', '.join(titles)

    class Meta:
        model = models.Author
        fields = ('id', 'firstname', 'lastname', 'nickname', 'birthdate',
                  'books_titles')
