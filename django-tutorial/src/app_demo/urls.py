from django.urls import path, include
from . import views


from rest_framework import routers
from app_demo.views import BookViewSet

router = routers.DefaultRouter()
router.register('books', BookViewSet)

urlpatterns = [
    path('func', views.view_000),
    path('class', views.View_000.as_view()),
    path('template/static', views.static_template),
    path('template/dynamic', views.dynamic_template),
    path('', include(router.urls))
]
