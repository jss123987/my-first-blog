from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm, signupform
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Post
from django.contrib.auth.models import User


def hello(request):
 posts = Post.objects.filter(published_date__isnull=False).order_by('published_date')
 return render(request, 'myapp/hello.html', {'posts':posts})

def unpublishedposts(request):
 PK=request.GET.get('PK', '85')
 f=Post.objects.get(pk=PK)
 ti=f.title
 c=f.caption
 t=f.Text
 t2=f.b
 t3=f.c
 t4=f.d
 t5=f.e
 t6=f.f
 t7=f.g
 t8=f.h
 t9=f.i
 t10=f.j
 t11=f.k
 t12=f.l
 t13=f.m
 if f.pk != 85:
   form=PostForm(request.POST, request.FILES, instance=f)
   if form.is_valid():
    post=form.save(commit=False)
    post.published_date = timezone.now()
    post.title=ti
    post.Text=t
    post.caption=c
    post.b=t2
    post.c=t3
    post.d=t4
    post.e=t5
    post.f=t6
    post.g=t7
    post.h=t8
    post.i=t9
    post.j=t10
    post.k=t11
    post.l=t12
    post.m=t13
    post.save()
    return redirect('post_detail',Pk=f.pk)
 else:
   posts=Post.objects.filter(published_date__isnull=True).filter(author=request.user)
   return render(request, 'myapp/unpublished.html', {'posts':posts})

def post_detail(request, Pk):
  post = get_object_or_404(Post, pk=Pk)
  return render(request, 'myapp/post_detail.html', {'post':post,})

def post_new(request):
 if request.method == "POST":
  form=PostForm(request.POST, request.FILES) 
  if form.is_valid():
   post = form.save(commit=False)
   post.author = request.user
   post.created_date = timezone.now()
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
   elif post.category=='Opinion':
    post.subcategory='Opinion'
   post.save()
   return redirect('post_detail', Pk=post.pk)
 else:
  form=PostForm()
  return render(request, 'myapp/post_edit.html',{'form':form})

def Post_Edit(request, PK):
 f=Post.objects.get(pk=PK)
 if request.method == "POST":
  form=PostForm(request.POST, request.FILES, instance=f)
  if form.is_valid():
   post = form.save(commit=False)
   post.lastedit=timezone.now()
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
   elif post.category=='Opinion':
    post.subcategory='Opinion'
   post.save()
   return redirect('post_detail', Pk=post.pk)
 else:
  form=PostForm(instance=f)
  return render(request, 'myapp/post_edit.html', {'form':form})

def ArcheologyCat(request, cat):
 posts= Post.objects.filter(category=cat)
 return render(request, 'myapp/cat_page.html', {'posts':posts})

def subcat(request, Subcategory):
 posts= Post.objects.filter(subcategory=Subcategory)
 return render(request, 'myapp/subcatpage.html',{'posts':posts})

def signup(request):
 if request.method=='POST':
  form=signupform(request.POST)
  if form.is_valid():
   form.save()
   username = form.cleaned_data.get('username')
   raw_password = form.cleaned_data.get('password1')
   user = authenticate(username=username, password=raw_password)
   login(request, user)
   return redirect('hello')
 else:
  form=signupform()
 return render(request, 'myapp/signup.html', {'form': form})

