from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm, signupform, yoo, postformset
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.forms.formsets import formset_factory
from django.forms import modelformset_factory
from .models import Post, yo

def hello(request):
 posts = Post.objects.all()
 return render(request, 'myapp/hello.html', {'posts':posts})

def post_detail(request, Pk):
  post = get_object_or_404(Post, pk=Pk)
  return render(request, 'myapp/post_detail.html', {'post':post,})

def post_new(request):
 if request.method == "POST":
  form=PostForm(request.POST, request.FILES) 
  form2=yoo(request.POST)
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
   elif post.category=='Opinion':
    post.subcategory='Opinion'
  if form2.is_valid:
   post2 = form2.save(commit=False)
   post2.save()
   post.text=post2
   post.save()
   return redirect('post_detail', Pk=post.pk)
 else:
  form=PostForm()
  form2 = yoo()
  return render(request, 'myapp/post_edit.html', {'form': form, 'form2':form2})

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
