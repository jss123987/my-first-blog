from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from django.utils import timezone

def hello(request):
 posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
 return render(request, 'myapp/hello.html', {'posts':posts})

def post_detail(request, pk):
 post = get_object_or_404(Post, pk=pk)
 return render(request, 'myapp/post_detail.html', {'post':post})
