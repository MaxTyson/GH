# Generated by Django 2.0.2 on 2018-02-10 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showstories', '0003_auto_20180210_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
