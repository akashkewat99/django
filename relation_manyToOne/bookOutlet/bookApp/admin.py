from django.contrib import admin

# Register your models here.
from .import models
from .models import Author,Book
from django.db import models

# class BookAdmin(admin.ModelAdmin):
#     readonly_fields = ('description')

admin.site.register(Author)
admin.site.register(Book)