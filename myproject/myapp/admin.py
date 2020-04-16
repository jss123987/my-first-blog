
# Register your models here.

from django.contrib import admin
from .models import Post, Profile, Messages

admin.site.register(Messages)
admin.site.register(Post)
admin.site.register(Profile)
