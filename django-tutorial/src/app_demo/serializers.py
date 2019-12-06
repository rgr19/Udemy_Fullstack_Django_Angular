from rest_framework import serializers
from . import models


class BookNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BookNumber
        fields = ['id', 'isbn_10', 'isbn_13']


class BookCharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BookCharacter
        fields = ['id', 'name']


class BookSerializer(serializers.ModelSerializer):
    number = BookNumberSerializer(many=False)
    character = BookCharacterSerializer(many=True)

    class Meta:
        model = models.Book
        fields = ['title', 'description', 'price', 'published', 'is_published',
                  'number', 'character']
