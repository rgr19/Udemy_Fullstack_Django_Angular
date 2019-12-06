from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from rest_framework import viewsets
from app_demo import serializers
from app_demo import models

# Create your views here.

from app_demo import models as app_demo_models


def view_000(request):
    return HttpResponse('View_000 message from views.')


class View_000(View):
    def get(self, request):
        return HttpResponse("This is another function inside class.")


def static_template(request):
    return render(request, 'static_template.html')


def dynamic_template(request):
    return render(request, 'dynamic_template.html',
                  dict(
                      data='This is some static string from python!',
                      books=app_demo_models.Book.objects.all(),
                  ))

from rest_framework.authentication import TokenAuthentication

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BookSerializer
    queryset = models.Book.objects.all()

    authentication_classes = (TokenAuthentication, )