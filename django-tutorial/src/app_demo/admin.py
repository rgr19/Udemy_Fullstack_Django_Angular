from django.contrib import admin
from . import models
# Register your models here.

# admin.site.register(models.Book) # to generic


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    # limit entry fields in website to
    # fields = ['title', 'description']

    # show those in Books list
    list_display = ['title', 'description', 'price']
    list_filter = ['published']
    search_fields = ['title', 'description']


admin.site.register(models.BookNumber)
admin.site.register(models.BookCharacter)


