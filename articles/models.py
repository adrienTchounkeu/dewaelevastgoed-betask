from django.db import models


class Article(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=32)
    slug = models.CharField(max_length=32, unique=True)
    content = models.TextField()

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.title


class Tag(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=32, unique=True)
    parent = models.ForeignKey('self', null=True, related_name='children', on_delete=models.CASCADE)
    article = models.ForeignKey(Article, null=True, related_name='article1', on_delete=models.CASCADE)
