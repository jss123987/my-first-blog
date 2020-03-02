from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import modelform_factory, modelformset_factory

class PostForm(forms.ModelForm):
 class Meta:
  model=Post
  widgets = {
            'text': forms.Textarea(attrs={'rows':10, 'cols':'25px', 'class':'postedittext', 'style':'padding-right:30.5px;', 'placeholder':'Enter content...',}),
            'title': forms.TextInput(attrs={'size':21, 'class':'postedittext', 'placeholder':'Enter title...', }),
  }
  fields = ('title', 'text', 'category',)

postformset=modelform_factory(Post, fields=('title','text','text','category'), form=PostForm,)

class signupform(UserCreationForm):
 password2=forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'size':21, 'placeholder':'Confirm password', 'class':'signupformtext',}))
 password1=forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'size':21, 'placeholder':'Enter your password', 'class':'signupformtext',}))
 username=forms.CharField(widget=forms.TextInput(attrs={'class':'signupformtext', 'size':21, 'placeholder':'Username',}))
 class Meta:
  model=User
  fields= ('username','password1','password2',)

