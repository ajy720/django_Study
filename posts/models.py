from django.db import models

# Create your models here.


class Post(models.Model):
    class Meta:
        ordering = ["-created_at"]  # 정렬 방법 1
        pass

    title = models.CharField(max_length=50)
    content = models.TextField()
    view_count = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
