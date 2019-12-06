from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

import app_api.models


class UserSerialized(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        token = Token.objects.create(user=user)
        print(f'Creating User {user} with token {token}')
        return user


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = app_api.models.Movie
        fields = ('id', *app_api.models.Movie.__slots__, 'no_of_ratings', 'avg_rating')


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = app_api.models.Rating
        fields = ('id', *app_api.models.Rating.__slots__)
