from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
# Create your views here.


def index(request):
    posts = Post.objects.all()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = PostForm()
    context = {
        "posts": posts,
        "form": form
    }
    return render(request, "myapp/index.html", context)
