# Generated by Django 5.0.4 on 2024-05-01 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cat', '0005_alter_cat_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='cat_photos/%Y/%m/', verbose_name='photo'),
        ),
    ]