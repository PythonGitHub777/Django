from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100,  verbose_name="عنوان:")
    author = models.CharField(max_length=100, blank=True, verbose_name="نویسنده:")
    text = models.TextField(verbose_name="متن:")
    create_time = models.DateTimeField(auto_now= True, verbose_name="متن:")
    cover = models.ImageField(upload_to = 'covers/', blank=False, verbose_name="عکس:")
