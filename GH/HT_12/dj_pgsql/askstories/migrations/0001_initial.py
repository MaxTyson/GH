# Generated by Django 2.0.1 on 2018-01-28 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Askstories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.CharField(max_length=20)),
                ('author', models.CharField(default=0, max_length=50)),
                ('score', models.IntegerField(default=0)),
                ('time', models.IntegerField(default=0)),
                ('title', models.CharField(default='', max_length=100)),
                ('type', models.CharField(default='', max_length=50)),
                ('url', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('url', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='askstories',
            name='category_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='askstories.Category'),
        ),
    ]
