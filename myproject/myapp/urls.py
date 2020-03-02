from django.urls import path
from . import views

urlpatterns = [
 path('', views.hello, name='hello'),
 path('post/<int:Pk>/', views.post_detail, name='post_detail'),
 path('post/new/', views.post_new, name='post_new'),
 path('cat/<str:cat>/', views.ArcheologyCat, name='CatPage'),
 path('subcat/<str:Subcategory>/', views.subcat, name='subcat'),
 path('signup/', views.signup, name='signup'),
]

