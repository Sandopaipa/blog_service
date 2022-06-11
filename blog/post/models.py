from django.db import models


class Post(models.Model):
    header = models.CharField(max_length=150)
    body = models.TextField
    author = models.ForeignKey
    publication_date = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.header
