from django.urls import path
from .views import new, create, show, edit, update, delete


app_name = "posts"
urlpatterns = [
    path("new/", new, name="new"),
    path("create/", create, name="create"),
    path("<int:post_id>/", show, name="show"),  # 꺽새 안에 주소를 통해 데이터 받을 수 있음 <자료형:변수명>
    path("edit/<int:post_id>", edit, name="edit"),
    path("update/<int:post_id>", update, name="update"),
    path("delete/<int:post_id>", delete, name="delete"),
]
