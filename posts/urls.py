from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.post, name='post'),
    path('author/<int:author_id>/', views.author, name='author'),
    path('api/posts/', views.post_list_create, name='post-list-create'), #posts/api/posts/
    path('api/posts/<int:pk>/', views.post_detail, name='post-detail'),
    path('api/authors/', views.author_list_create, name='author-list-create'),
    path('api/authors/<int:pk>/', views.author_detail, name='author-detail'),


    # path('posts/', include('posts.urls')),
] 