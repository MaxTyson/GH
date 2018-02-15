# Generated by Django 2.0.2 on 2018-02-15 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('showstories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jobstories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.CharField(max_length=20)),
                ('author', models.CharField(default=0, max_length=50)),
                ('score', models.IntegerField(default=0)),
                ('time', models.IntegerField(default=0)),
                ('title', models.CharField(default='', max_length=100)),
                ('type', models.CharField(default='', max_length=50)),
                ('url', models.CharField(max_length=200)),
                ('category_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='showstories.Cat')),
            ],
        ),
    ]
