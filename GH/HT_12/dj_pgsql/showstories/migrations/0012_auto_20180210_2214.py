# Generated by Django 2.0.2 on 2018-02-10 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showstories', '0011_auto_20180210_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='showstories',
            name='time',
            field=models.DateTimeField(),
        ),
    ]