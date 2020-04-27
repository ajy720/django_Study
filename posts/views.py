from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
import pdb


def main(request):
    context = {
        "posts": Post.objects.all(),  # 정렬 방법 1. models.py에서 해주는 방법
        # "posts": Post.objects.order_by("-created_at"), # 정렬 방법 2
    }
    return render(request, "posts/main.html", context)


def new(request):
    context = {"form": PostForm()}
    return render(request, "posts/new.html", context)


def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect("main")


def show(request, post_id):  # 방법 2. 주소에서 값 전달 -> urls.py에서 post_id 전달해준거 받기
    # 방법 1
    # post_id = request.GET.get("post_id")  # 받은 url에서 post_id라는 인자 값 얻고
    post = Post.objects.get(
        id=post_id
    )  # Post 객체들 중에 해당 post_id를 id(Primary key)로 갖고 있는 친구를 찾아서
    context = {"post": post}  # context에 딕셔너리 형태로 넣어주고

    return render(request, "posts/show.html", context)  # 템플릿에 전달하면 해당 html(템플릿) 안에서 출력
