from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.

class Movie(models.Model):
    __slots__ = ('title', 'description')

    title = models.CharField(max_length=32)
    description = models.TextField(max_length=360)

    def __str__(self):
        return f"Movie({self.title})"

    def __repr__(self):
        return f"Movie(title={self.title}, description='{self.description}')"

    @property
    def no_of_ratings(self):
        return Rating.objects.filter(movie=self).count()

    @property
    def avg_rating(self):
        k, v = Rating.objects.filter(movie=self).aggregate(models.Avg('stars')).popitem()
        return v


class Rating(models.Model):
    __slots__ = ('movie', 'user', 'stars')

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = (('user', 'movie'),)
        index_together = (('user', 'movie'),)

    def __str__(self):
        return f"Rating(movie:{self.movie}, user:{self.user}, stars:{self.stars})"

    def __repr__(self):
        return self.__str__()
