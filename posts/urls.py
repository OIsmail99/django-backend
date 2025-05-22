from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api/auth/register/', views.register, name='register'),
    path('api/auth/login/', views.login, name='login'),
    path('api/auth/logout/', views.logout, name='logout'),
    path('api/posts/', views.post_list_create, name='post-list-create'), #posts/api/posts/
    path('api/posts/<int:pk>/', views.post_detail, name='post-detail'),
    path('api/users/', views.user_list_create, name='user-list-create'),
    path('api/users/<int:pk>/', views.user_detail, name='user-detail'),


    # path('posts/', include('posts.urls')),
]