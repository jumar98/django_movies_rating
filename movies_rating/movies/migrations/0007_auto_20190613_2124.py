# Generated by Django 2.2 on 2019-06-13 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_auto_20190613_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='detail',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
