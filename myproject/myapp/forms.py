from django import forms
from .models import Post

class PostForm(forms.ModelForm):
 class Meta:
  model = Post
  widgets = {
            'text': forms.Textarea(attrs={'rows':4, 'cols':15}),
  }
  fields = ('title', 'text', 'category',)
