from django.db import models
# .filter Showstories
# from up1 item=item.obj.filter

# Create your models here.
class Cat(models.Model):
    name = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Showstories(models.Model):
    category_fk = models.ForeignKey(Cat, on_delete=models.CASCADE)

    item_id = models.CharField(max_length=20)
    author = models.CharField(max_length=50, default=0)
    score= models.IntegerField(default=0)
    time = models.CharField(max_length=20, default='')
    title = models.CharField(max_length=100, default='')
    type = models.CharField(max_length=50, default='')
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.title



# item = Category.object.all