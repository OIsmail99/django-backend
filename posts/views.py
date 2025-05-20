from django.http import HttpResponse
from django.shortcuts import render
from .models import Post, Comment, Author
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostSerializer, AuthorSerializer
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
def author_list_create(request):
    if request.method == 'GET':
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True) #many=True means we are getting multiple authors
        return Response(serializer.data) 
    elif request.method == 'POST':
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH', 'DELETE'])
def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'GET':
        serializer = AuthorSerializer(author)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = AuthorSerializer(author, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




def index(request):
    return render(request, 'posts/index.html', {'posts': posts})

def post(request, post_id):
    post = posts.filter(id=post_id).first()
    if post:
        return render(request, 'posts/post.html', {'post': post})
    else:
        return HttpResponse("Post not found.")

def author(request, author_id):
    author = Author.objects.get(id=author_id)
    if author:
        return render(request, 'posts/author.html', {'author': author})
    else:
        return HttpResponse("Author not found.")