from django.http import HttpResponse
from django.shortcuts import render
from .models import Post, Comment
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostSerializer, UserSerializer, CommentSerializer
from django.shortcuts import get_object_or_404

# Create your views here.


@api_view(['GET', 'POST'])
def post_list_create(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) #or just status=201
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


@api_view(['GET', 'PATCH', 'DELETE'])
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid(): 
            serializer.save() #saving to db
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def user_list_create(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data) 
    elif request.method == 'POST':
        # Extract username and password
        username = request.data.get('username')
        password = request.data.get('password')
        
        # Create user with properly hashed password
        user = User.objects.create_user(username=username, password=password)
        
        # Return serialized user (without password)
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PATCH', 'DELETE'])
def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




# def index(request):
#     return render(request, 'posts/index.html', {'posts': posts})

# def post(request, post_id):
#     post = posts.filter(id=post_id).first()
#     if post:
#         return render(request, 'posts/post.html', {'post': post})
#     else:
#         return HttpResponse("Post not found.")

# def author(request, author_id):
#     user = get_object_or_404(User, id=author_id)
#     return render(request, 'posts/author.html', {'author': user})