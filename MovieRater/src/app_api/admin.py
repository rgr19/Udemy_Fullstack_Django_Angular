from django.contrib import admin

# Register your models here.
import app_api.models as models

admin.site.register(models.Movie)
admin.site.register(models.Rating)
