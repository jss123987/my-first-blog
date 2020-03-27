from django.urls import path
from . import views
from . import models
from myapp.forms import loginform
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
 path('', views.hello, name='hello'),
 path('post/<int:Pk>/', views.post_detail, name='post_detail'),
 path('post/new/', views.post_new, name='post_new'),
 path('cat/<str:cat>/', views.ArcheologyCat, name='CatPage'),
 path('subcat/<str:Subcategory>/', views.subcat, name='subcat'),
 path('signup/', views.signup, name='signup'),
 path('login/', auth_views.LoginView.as_view(authentication_form=loginform), name='login'),
 path('logout/', auth_views.LogoutView.as_view(), name='logout'),
 path('post/edit/<int:PK>/', views.Post_Edit, name='postedit'),
 path('posts/unpublished/', views.unpublishedposts, name='unpublished'),
 path('delete/<int:PK>/', views.deletepost, name='deletepost'),
 path('createprofile/', views.createprofile, name='createprofile'),
 path('profile/<int:userpk>/', views.profile, name='profilepage'),
 path('profile/edit/<int:profilepk>/', views.editprofile, name='editprofile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
