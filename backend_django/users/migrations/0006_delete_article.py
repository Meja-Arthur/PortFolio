# Generated by Django 4.2.2 on 2023-07-25 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_article'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Article',
        ),
    ]