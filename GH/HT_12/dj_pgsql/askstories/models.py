from django.db import models

# Create your models here.
class Askstories(models.Model):

    item_id = models.CharField(max_length=20)
    author = models.CharField(max_length=50, default=0)
    score= models.IntegerField(default=0)
    time = models.IntegerField(default=0)
    title = models.CharField(max_length=100, default='')
    type = models.CharField(max_length=50, default='')
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.title