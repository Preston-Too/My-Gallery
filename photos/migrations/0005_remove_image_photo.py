# Generated by Django 3.1.5 on 2021-01-11 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_image_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='photo',
        ),
    ]
