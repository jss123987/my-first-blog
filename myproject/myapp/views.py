from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm

def hello(request):
 posts = Post.objects.order_by('published_date')
 return render(request, 'myapp/hello.html', {'posts':posts})

def post_detail(request, pk):
 post = get_object_or_404(Post, pk=pk)
 return render(request, 'myapp/post_detail.html', {'post':post})

def post_new(request):
 form = PostForm()
 return render(request, 'myapp/post_edit.html', {'form': form})

