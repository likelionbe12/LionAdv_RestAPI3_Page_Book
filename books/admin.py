from django.contrib import admin
from .models import Category, Book, BookLoan
# Register your models here.
admin.site.register([Category, Book, BookLoan])