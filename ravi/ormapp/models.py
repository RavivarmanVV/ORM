from django.db import models
from django.contrib import admin

class Book(models.Model):
  Name= models.CharField(max_length=100)
  Email= models.EmailField()
  Book_No= models.CharField(max_length=100)
  Book_Name= models.CharField(max_length=100)
  Address= models.CharField(max_length=255)
  Phone_No= models.CharField(max_length=15)
class BookAdmin(admin.ModelAdmin):
    list_display = ('Name','Email','Book_No','Book_Name','Address','Phone_No')