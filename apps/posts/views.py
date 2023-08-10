from rest_framework import generics
from apps.posts.models import Post  
from apps.posts.serializers import PostSerilizer
# Create your views here.

class PostAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerilizer

class PostCreateAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerilizer