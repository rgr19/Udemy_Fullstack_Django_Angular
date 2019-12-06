from django.db import models
from django.utils import timezone
from django.conf import settings
from django.conf.urls.static import static
# Create your models here.
import os
import time
import datetime


class BookNumber(models.Model):
    isbn_10 = models.CharField(max_length=10, blank=True)
    isbn_13 = models.CharField(max_length=13, blank=True)

    def __str__(self):
        return str(self.id)

class Book(models.Model):
    BOOKS = (
        ('HB', 'Hobbit'),
        ('LOTR', 'Lord of the rings'),
        ('HAT', 'Here and there'),
    )
    title = models.CharField(max_length=36,
                             choices=BOOKS,
                             blank=False,
                             unique=True,
                             default=BOOKS[-1],
                             )

    description = models.TextField(max_length=256, blank=True)
    price = models.DecimalField(max_digits=4, default=0, decimal_places=2)
    discount = models.FloatField(default=1)
    quantity = models.IntegerField(default=1)
    something = models.BigIntegerField(default=0)
    # created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.DateField(default=timezone.now)
    is_published = models.BooleanField(default=True)
    file = models.FileField(null=True, upload_to='files/', blank=True)
    cover = models.ImageField(null=True, upload_to='covers/', blank=True)

    number = models.OneToOneField(BookNumber, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class BookCharacter(models.Model):
    name = models.CharField(max_length=30)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='character')

    def __str__(self):
        return self.name


