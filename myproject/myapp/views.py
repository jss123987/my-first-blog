from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Profile, Messages
from django.utils import timezone
from .forms import PostForm, signupform, loginform, CreateProfile, SendMessage
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Post
from django.contrib.auth.models import User
from django.template import Context, loader

def messenger(request, recipient):
 user=request.user
 rec=User.objects.get(username=recipient)
 sender=Profile.objects.get(Username=rec)
 return render(request, 'myapp/message.html', {'recipient':recipient,'user':user,'sender':sender})

def messengerxml(request, recipient):
 if request.method=='POST':
  form=SendMessage(request.POST)
  if form.is_valid:
   post=form.save(commit=False)
   post.recipient = User.objects.get(username=recipient)
   post.author = request.user
   post.published_date = timezone.now()
   post.save()
 else:
  poststo=Messages.objects.filter(author=request.user).filter(recipient=User.objects.get(username=recipient))
  postsfrom=Messages.objects.filter(recipient=request.user).filter(author=User.objects.get(username=recipient))
  t = loader.get_template('myapp/message.xml')
  c = {'poststo':poststo,'postsfrom':postsfrom,}
  return HttpResponse(t.render(c), content_type='application/xml')

def helloxml(request):
 t = loader.get_template('myapp/hello.xml')
 posts =Post.objects.filter(published_date__isnull=False).order_by('published_date').reverse()
 c = {'posts':posts}
 return HttpResponse(t.render(c), content_type='application/xml')

def hello(request):
 posts = Post.objects.filter(published_date__isnull=False).order_by('published_date').reverse()
 return render(request, 'myapp/hello.html', {'posts':posts})

def about(request):
    return render(request, 'myapp/about.html')

def createprofile(request):
 if request.method == "POST":
  form=CreateProfile(request.POST, request.FILES)
  if form.is_valid():
   post = form.save(commit=False)
   post.Username = request.user
   post.EmailAddress = request.user.email
   post.save()
   return redirect('hello')
  else:
   return render(request, 'myapp/createprofile.html', {'form':form})
 else:
  form=CreateProfile()
  user=request.user
  if user.is_authenticated:
   count=Profile.objects.filter(Username = request.user).count()
  else:
   count=True
  return render(request, 'myapp/createprofile.html',{'form':form,'count':count,})

def deletepost(request, PK):
 Post.objects.get(pk=PK).delete()
 return redirect('hello')

def editprofile(request, profilepk):
 f=Profile.objects.get(pk=profilepk)
 pk=f.pk
 if request.user.pk == f.Username.pk:
  if request.method == "POST":
   form=CreateProfile(request.POST, request.FILES, instance=f)
   if form.is_valid():
    post = form.save(commit=False)
    post.save()
    return redirect('hello')
   else:
    return render(request, 'myapp/createprofile.html', {'form':form,'pk':pk,})
  else:
   form=CreateProfile(instance=f)
   user=request.user
   return render(request, 'myapp/createprofile.html',{'form':form,'pk':pk,})
 else:
  return HttpResponse('You can only edit you own profile!')


def profile(request, userpk):
 users=User.objects.get(pk=userpk)
 profile=Profile.objects.get(Username=users)
 profileposts=Post.objects.filter(author=users, published_date__isnull=False).order_by('published_date').reverse()
 return render(request, 'myapp/profile.html', {'profile':profile, 'profileposts':profileposts,})


def unpublishedposts(request):
 PK=request.GET.get('PK', '19')
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
 if f.pk != 19:
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
   posts=Post.objects.filter(published_date__isnull=True).filter(author=request.user).order_by('created_date').reverse().exclude(pk=19)
   return render(request, 'myapp/unpublished.html', {'posts':posts})

def post_detail(request, Pk):
  post = get_object_or_404(Post, pk=Pk)
  user=request.user
  return render(request, 'myapp/post_detail.html', {'post':post,'user':user,})

def post_new(request):
 if request.method == "POST":
  form=PostForm(request.POST, request.FILES) 
  if 'save' in request.POST:
   if form.is_valid():
    post = form.save(commit=False)
    post.author = request.user
    post.created_date = timezone.now()
    post.lastedit = timezone.now()
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
    return  messages.error(request, "Error")
  if 'publish' in request.POST:
   if form.is_valid():
    post = form.save(commit=False)
    post.author = request.user
    post.created_date = timezone.now()
    post.published_date = timezone.now()
    post.lastedit = timezone.now()
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
 usert=request.user
 a=f.author
 p=f.published_date
 p1=f.b
 p2=f.c
 p3=f.d
 p4=f.e
 p5=f.f
 p6=f.g
 p7=f.h
 p8=f.i
 p9=f.j
 p10=f.k
 p11=f.l
 p12=f.m
 pk=f.pk
 if request.method == "POST":
  form=PostForm(request.POST, request.FILES, instance=f)
  if 'save' in request.POST:
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
    if usert != post.author:
     post.contributers.add(request.user)
    return redirect('post_detail', Pk=post.pk)
  if 'publish' in request.POST:
   if form.is_valid():
    post = form.save(commit=False)
    post.author = request.user
    post.created_date = timezone.now()
    post.published_date = timezone.now()
    post.lastedit = timezone.now()
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
  return render(request, 'myapp/post_edit.html', {'form':form, 'p':p,'p1':p1,'p2':p2,'p3':p3,'p4':p4,'p5':p5,'p6':p6,'p7':p7,'p8':p8,'p9':p9,'p10':p10,'p11':p11,'p12':p12,'pk':pk,})

def ArcheologyCat(request, cat):
 posts= Post.objects.filter(category=cat).order_by('published_date').reverse()
 return render(request, 'myapp/cat_page.html', {'posts':posts, 'cat':cat})

def subcat(request, Subcategory):
 posts= Post.objects.filter(subcategory=Subcategory).order_by('published_date').reverse()
 return render(request, 'myapp/subcatpage.html',{'posts':posts, 'Subcategory':Subcategory})

def signup(request):
 if request.method=='POST':
  form=signupform(request.POST)
  if form.is_valid():
   form.save()
   username = form.cleaned_data.get('username')
   raw_password = form.cleaned_data.get('password1')
   user = authenticate(username=username, password=raw_password)
   login(request, user)
   return redirect('createprofile')
 else:
  form=signupform()
 return render(request, 'myapp/signup.html', {'form': form})

