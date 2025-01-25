from django.db import models
from django.utils import timezone
from datetime import timedelta


class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, related_name="posts", null=True,
                               blank=True, on_delete=models.SET_NULL)

    def published_recently(self):
        return timezone.now() - timedelta(days=7) < self.published_date

    def __str__(self):
        return self.title
