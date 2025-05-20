from rest_framework import serializers
from .models import Post, Author, Comment

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
    
    def validate_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Name should only contain alphabets.")
        return value
    

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
