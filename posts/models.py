from django.db import models
from django.urls import reverse

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

    def __str__(self):
        return self.title

    def get_absolute_url(
        self,
    ):  # 자동으로 해당 url을 반환해주는 함수. 수동 호출이 아닌 자동 호출. 추후 클래스 베이스드 뷰에서 디테일 뷰에 자동 연결
        return reverse("posts:show", args=[self.id])
