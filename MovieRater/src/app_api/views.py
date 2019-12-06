# Create your views here.
import inspect
from pprint import pprint

import rest_framework.authentication
import rest_framework.decorators
import rest_framework.permissions
import rest_framework.response
import rest_framework.status
from django.contrib.auth.models import User
from rest_framework import viewsets

from app_api import models
from app_api import serializers


def inspect_object(o) -> None:
    pprint(
        f"The type is {type(o)}\n:"
        f"INSPECT {inspect.getmro(type(o))}\n"
        f"DIR {dir(o)}\n"
    )


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerialized


def bad_request_response(message):
    response = dict(message=message)
    status = rest_framework.status.HTTP_400_BAD_REQUEST
    return rest_framework.response.Response(response, status=status)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer
    permission_classes = (rest_framework.permissions.AllowAny,)
    authentication_classes = (rest_framework.authentication.TokenAuthentication,)

    @rest_framework.decorators.action(detail=True, methods=['POST'],
                                      permission_classes=(rest_framework.permissions.IsAuthenticated,))
    def rate_movie(self, request, pk=None):

        if 'stars' not in request.data:
            return bad_request_response('You need to request `stars`')

        print(f'Primary key `{pk}` received at `rate_movie`')

        movie = models.Movie.objects.get(id=pk)
        stars = request.data['stars']
        user = request.user

        print(f'POST : User `{user}` rating of movie `{movie}` with stars `{stars}`.')

        # app_api.models.Rating.objects.get():

        rating, isCreated = models.Rating.objects.update_or_create(user_id=user.id, user=user,
                                                                   movie_id=movie.id, movie=movie,
                                                                   defaults=dict(stars=stars))
        ratingSerialized = serializers.RatingSerializer(rating, many=False)

        response = {
            'message': 'Rating created.' if isCreated else 'Rating updated',
            'result': ratingSerialized.data,
        }

        status = rest_framework.status.HTTP_200_OK
        return rest_framework.response.Response(response, status=status)

    @rest_framework.decorators.action(detail=True, methods=['POST'])
    def rate_movie_anonymous(self, request, pk=None):

        if 'stars' not in request.data:
            return bad_request_response('You need to request `stars`')

        print(f'Primary key `{pk}` received at `rate_movie`')

        movie = models.Movie.objects.get(id=pk)
        stars = request.data['stars']
        user = request.user
        if user.is_anonymous:
            user = models.User.objects.get(id=1)

        print(f'POST : User `{user}` rating of movie `{movie}` with stars `{stars}`.')

        # app_api.models.Rating.objects.get():

        rating, isCreated = models.Rating.objects.update_or_create(user_id=user.id, user=user,
                                                                   movie_id=movie.id, movie=movie,
                                                                   defaults=dict(stars=stars))
        ratingSerialized = serializers.RatingSerializer(rating, many=False)

        response = {
            'message': 'Rating created.' if isCreated else 'Rating updated',
            'result': ratingSerialized.data,
        }

        status = rest_framework.status.HTTP_200_OK
        return rest_framework.response.Response(response, status=status)

    @rest_framework.decorators.action(detail=False, methods=['POST'])
    def rate_movies(self, request, pk=None):
        print(f'Primary key {pk} received at `rate_movies`')
        response = {'message': 'its working'}
        return rest_framework.response.Response(response, status=rest_framework.status.HTTP_200_OK)



class RatingViewSet(viewsets.ModelViewSet):
    queryset = models.Rating.objects.all()
    serializer_class = serializers.RatingSerializer
    permission_classes = (rest_framework.permissions.IsAuthenticated,)
    authentication_classes = (rest_framework.authentication.TokenAuthentication,)

    def update(self, request, *args, **kwargs):
        return bad_request_response(f"{self}.update is disabled.")

    def create(self, request, *args, **kwargs):
        return bad_request_response(f"{self}.create is disabled.")
