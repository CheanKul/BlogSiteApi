
from django.db import models


class Post(models.Model):
    """ Post Related """
    Header = models.CharField(max_length=300, null=True)
    SubTitile = models.CharField(max_length=300, null=True)
    ImgURL = models.CharField(max_length=300, null=True)
    Content = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.Header
