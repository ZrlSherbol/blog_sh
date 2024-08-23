from django.shortcuts import render, redirect

from posts.form import PostForm
from posts.models import Post


def main_view(request):
    if request.method == 'GET':
        return render(request, 'main.html')

def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        return render(request, 'posts/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    if request.method == 'GET':
        post = Post.objects.get(id=post_id)
        return render(request, 'posts/post_detail.html', context={"post": post})

def post_create(request):
    if request.method == 'GET':
        form = PostForm
        return render(request, 'posts/post_create.html', context={"form": form})
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, 'posts/post_create.html', context={"form": form})
        image = form.cleaned_data.get('image')
        title = form.cleaned_data.get('title')
        content = form.cleaned_data.get('content')
        rate = form.cleaned_data.get('rate')
        Post.objects.create(
            image=image,
            title=title,
            content=content,
            rate=rate
        )
        return redirect("/posts/")
