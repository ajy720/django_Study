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
