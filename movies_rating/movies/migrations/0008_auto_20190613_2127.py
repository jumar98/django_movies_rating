# Generated by Django 2.2 on 2019-06-13 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_auto_20190613_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='detail',
            field=models.TextField(),
        ),
    ]
