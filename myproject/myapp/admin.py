
# Register your models here.

from django.contrib import admin
from .models import Post, login, yo

admin.site.register(Post)
admin.site.register(login)
admin.site.register(yo)
