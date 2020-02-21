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
   if post.category=='Religion':
    post.subcategory='World'
   elif post.category=='Disaster':
    post.subcategory='World'
   elif post.category=='Environment':
    post.subcategory='World'
   elif post.category=='Conflicts':
    post.subcategory='World'
   elif post.category=='Scandals':
    post.subcategory='World'
   elif post.category=='Crime':
    post.subcategory='U.S.'
   elif post.category=='Education':
    post.subcategory='U.S.'
   elif post.category=='Immigration':
    post.subcategory='U.S.'
   elif post.category=='Music News':
    post.subcategory='Entertainment'
   elif post.category=='Celebrity News':
    post.subcategory='Entertainment'
   elif post.category=='Archeology':
    post.subcategory='Science'
   elif post.category=='Wild Nature':
    post.subcategory='Science'
   elif post.category=='Natural Science':
    post.subcategory='Science'
   post.save()
   return redirect('post_detail', Pk=post.pk)
 else:
  form = PostForm()
 return render(request, 'myapp/post_edit.html', {'form': form})

def ArcheologyCat(request, cat):
 posts= Post.objects.filter(category=cat)
 return render(request, 'myapp/cat_page.html', {'posts':posts})

def subcat(request, Subcategory):
 posts= Post.objects.filter(subcategory=Subcategory)
 return render(request, 'myapp/subcatpage.html',{'posts':posts})

