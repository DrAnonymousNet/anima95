from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.


def home(request):
    return render(request, 'animation/index.html')


def animation(request):
    all_posts = Post.newmanager.all()

    return render(request, 'animation/animation.html', {'posts': all_posts})


def documentation(request):
    return render(request, 'animation/documentation.html')


def logout(request):
    return render(request, 'animation/index.html')
