from django.db import models
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    class Meta:
        ordering = ["-created_at"]  # 정렬 방법 1
        pass

    POST_TYPES = [
        (0, "칼럼"),
        (1, "뉴스"),
        (2, "소설"),
    ]

    title = models.CharField(max_length=50, verbose_name="제목")
    content = models.TextField(verbose_name="내용")
    view_count = models.IntegerField(default=0, verbose_name="조회수")

    _type = models.PositiveSmallIntegerField(choices=POST_TYPES, verbose_name="게시글 종류")

    image = models.ImageField(
        upload_to="posts/img",
        default="posts/default/default_img.jpg",
        verbose_name="이미지",
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="등록 시간")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정 시간")

    def __str__(self):
        return self.title

    # 자동으로 해당 url을 반환해주는 함수. 수동 호출이 아닌 자동 호출. 추후 클래스 베이스드 뷰에서 디테일 뷰에 자동 연결
    def get_absolute_url(self,):
        return reverse("posts:show", args=[self.id])
