from django.db import models

class Photo(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')
    url = models.URLField(default='')

    def __str__(self):
        return self.title


class Like(models.Model):
    photo_name = models.ForeignKey(Photo, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.photo_name