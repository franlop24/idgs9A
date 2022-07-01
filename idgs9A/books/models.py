from django.db import models

# Create your models here.
class Books(models.Model):
    title_book = models.TextField()
    author_book = models.TextField()
    count_sale_book = models.TextField()
    image_book = models.TextField()

class Users(models.Model):
    user_name = models.TextField()
    user_lastName = models.TextField()
    user_addres = models.TextField()
    user_celphone = models.TextField()
    reference_bookUser = models.TextField()
    user_status = models.BooleanField()