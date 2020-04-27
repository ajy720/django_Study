from django.urls import path
from .views import new, create, show

app_name = "posts"
urlpatterns = [
    path("new/", new, name="new"),
    path("create/", create, name="create"),
    path("<int:post_id>/", show, name="show"),  # 꺽새 안에 주소를 통해 데이터 받을 수 있음 <자료형:변수명>
]
