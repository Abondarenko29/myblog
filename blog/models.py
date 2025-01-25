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


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments",
                             on_delete=models.CASCADE)
    text = models.TextField(blank=False, null=False)
    author = models.ForeignKey(Author, related_name="author",
                               on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.author} in {self.post}"
