# Generated by Django 2.0.2 on 2018-02-10 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showstories', '0005_auto_20180210_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='url',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='showstories',
            name='category_fk',
            field=models.ForeignKey(default=0, on_delete='CASCADE', to='showstories.Category'),
        ),
    ]
