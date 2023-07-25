# Generated by Django 4.2.2 on 2023-07-25 10:05

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_delete_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', tinymce.models.HTMLField(verbose_name='Content')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
