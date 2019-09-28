from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()

    def __str__(self):
        return f"{self.title}"
