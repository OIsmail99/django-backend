from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='posts', null=True, blank=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment on {self.post.title} by {self.created_at}'
    
class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
