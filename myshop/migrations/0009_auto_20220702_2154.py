# Generated by Django 3.2.12 on 2022-07-02 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0008_wishlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='image_135x135',
        ),
        migrations.RemoveField(
            model_name='products',
            name='image_330x330',
        ),
    ]
