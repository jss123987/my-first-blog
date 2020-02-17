from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm

def hello(request):
 posts = Post.objects.order_by('published_date')
 return render(request, 'myapp/hello.html', {'posts':posts})

def post_detail(request, Pk):
 post = get_object_or_404(Post, pk=Pk)
 return render(request, 'myapp/post_detail.html', {'post':post})

def post_new(request):
 if request.method == "POST":
  form = PostForm(request.POST)
  if form.is_valid():
   post = form.save(commit=False)
   post.author = request.user
   post.published_date = timezone.now()
   post.save()
   return redirect('post_detail', pk=post.pk)
 else:
  form = PostForm()
 return render(request, 'myapp/post_edit.html', {'form': form})

def ArcheologyCat(request, cat):
 post= Post.objects.filter(category=cat)
 return render(request, 'myapp/cat_page.html', {'post':post})
