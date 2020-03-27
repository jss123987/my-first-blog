from django import forms
from .models import Post, Profile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.validators import validate_email


class CreateProfile(forms.ModelForm):
 Firstname=forms.CharField(label='First name', widget=forms.TextInput(attrs={'size':21, 'class':'postedittext', 'placeholder':'Enter first name...', }),)
 Lastname=forms.CharField(label='Last name', widget=forms.TextInput(attrs={'size':21, 'class':'postedittext', 'placeholder':'Enter last name...', }),)
 profilepic=forms.FileInput()
 class Meta:
  model=Profile
  widgets = {'Bio': forms.Textarea(attrs={'rows':10, 'cols':'25px', 'class':'postedittext', 'style':'padding-right:30.5px;', 'placeholder':'Enter content...',}),}

  fields =('Firstname', 'Lastname', 'Bio', 'profilepic',)

class PostForm(forms.ModelForm):
 class Meta:
  model=Post
  widgets = {
            'title': forms.TextInput(attrs={'size':21, 'class':'postedittext', 'placeholder':'Enter title...', }),
	    'caption': forms.TextInput(attrs={'size':21, 'class':'postedittext', 'placeholder':'Enter caption...', }),
            'Text': forms.Textarea(attrs={'rows':10, 'cols':'25px', 'class':'postedittext', 'style':'padding-right:30.5px;', 'placeholder':'Enter content...',}),
	    'b': forms.Textarea(attrs={'rows':10, 'cols':'25px', 'class':'postedittext', 'style':'padding-right:30.5px;', 'placeholder':'Enter content...',}),
	    'c': forms.Textarea(attrs={'rows':10, 'cols':'25px', 'class':'postedittext', 'style':'padding-right:30.5px;', 'placeholder':'Enter content...',}),
	    'd': forms.Textarea(attrs={'rows':10, 'cols':'25px', 'class':'postedittext', 'style':'padding-right:30.5px;', 'placeholder':'Enter content...',}),
	    'e': forms.Textarea(attrs={'rows':10, 'cols':'25px', 'class':'postedittext', 'style':'padding-right:30.5px;', 'placeholder':'Enter content...',}),
	    'f': forms.Textarea(attrs={'rows':10, 'cols':'25px', 'class':'postedittext', 'style':'padding-right:30.5px;', 'placeholder':'Enter content...',}),
	    'g': forms.Textarea(attrs={'rows':10, 'cols':'25px', 'class':'postedittext', 'style':'padding-right:30.5px;', 'placeholder':'Enter content...',}),
	    'h': forms.Textarea(attrs={'rows':10, 'cols':'25px', 'class':'postedittext', 'style':'padding-right:30.5px;', 'placeholder':'Enter content...',}),
	    'i': forms.Textarea(attrs={'rows':10, 'cols':'25px', 'class':'postedittext', 'style':'padding-right:30.5px;', 'placeholder':'Enter content...',}),
	    'j': forms.Textarea(attrs={'rows':10, 'cols':'25px', 'class':'postedittext', 'style':'padding-right:30.5px;', 'placeholder':'Enter content...',}),
	    'k': forms.Textarea(attrs={'rows':10, 'cols':'25px', 'class':'postedittext', 'style':'padding-right:30.5px;', 'placeholder':'Enter content...',}),
	    'l': forms.Textarea(attrs={'rows':10, 'cols':'25px', 'class':'postedittext', 'style':'padding-right:30.5px;', 'placeholder':'Enter content...',}),
	    'm': forms.Textarea(attrs={'rows':10, 'cols':'25px', 'class':'postedittext', 'style':'padding-right:30.5px;', 'placeholder':'Enter content...',}),
            }

  fields =('title','category','upload','caption','Text','b','c','d','e','f','g','h','i','j','k','l','m','p1','p2','p3','p4','p5','p6','p7','p8','p9','p10','p11','p12','p13',)

class signupform(UserCreationForm):
 password2=forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'size':21, 'placeholder':'Confirm password', 'class':'signupformtext',}))
 password1=forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'size':21, 'placeholder':'Enter your password', 'class':'signupformtext',}))
 username=forms.CharField(widget=forms.TextInput(attrs={'class':'signupformtext','size':21, 'placeholder':'Username',}))
 email=forms.EmailField(label='Email Address', widget=forms.TextInput(attrs={'size':21, 'class':'postedittext', 'placeholder':'Enter email address...', }),)

 def clean(self):
  cleaned_data = super(signupform, self).clean()
  email_passed = cleaned_data.get("email")
  if User.objects.filter(email=email_passed).count():
   raise forms.ValidationError("Account with that email address has already been created",)

 class Meta:
  model=User
  fields= ('username','password1','password2','email',)

class loginform(AuthenticationForm):
 def __init__(self, *args, **kwargs):
  super(loginform, self).__init__(*args, **kwargs)

 password=forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'size':21, 'placeholder':'Enter your password', 'class':'signupformtext',}))
 username=forms.CharField(widget=forms.TextInput(attrs={'class':'signupformtext','size':21, 'placeholder':'Username',}))

