# Generated by Django 4.2.3 on 2023-07-24 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0003_movie_language_alter_movie_desc_alter_movie_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='language',
            field=models.CharField(max_length=10),
        ),
    ]
