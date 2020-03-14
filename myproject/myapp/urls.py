from django.urls import path
from . import views
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
 path('login/', auth_views.LoginView.as_view(), name='login'),
 path('logout/', auth_views.LogoutView.as_view(), name='logout'),
 path('post/edit/<int:PK>/', views.Post_Edit, name='postedit'),
 path('posts/unpublished/', views.unpublishedposts, name='unpublished'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
