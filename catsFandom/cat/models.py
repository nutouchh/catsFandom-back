from autoslug import AutoSlugField
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

from rest_framework.validators import UniqueValidator

def get_upload_path(instance, filename):
    slug = instance.slug
    user = instance.user.username if instance.user else 'unknown_user'
    extension = filename.split('.')[-1]
    current_date = datetime.now()
    year_month = current_date.strftime('%Y/%m')

    return f'cat_photos/{year_month}/{slug}-{user}.{extension}'

class Cat(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    # category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', null=True,  on_delete=models.SET_NULL)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    photo = models.ImageField(upload_to=get_upload_path, null=True, blank=True, verbose_name="photo")
    born_year = models.IntegerField(null=True, blank=True, verbose_name="Год рождения")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-is_published', 'title']
#
# class Category(models.Model):
#     name = models.CharField(max_length=100, db_index=True)
#
#     def __str__(self):
#         return self.name

