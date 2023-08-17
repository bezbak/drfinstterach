from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from apps.posts.models import Post  
from apps.posts.serializers import PostSerilizer
# Create your views here.

#!  class PostAPIView(generics.ListAPIView):
#!      queryset = Post.objects.all()
#!      serializer_class = PostSerilizer

#!  class PostCreateAPIView(generics.CreateAPIView):
#!      queryset = Post.objects.all()
#!      serializer_class = PostSerilizer

#!  class PostUpdateAPIView(generics.UpdateAPIView):
#!      queryset = Post.objects.all()
#!      serializer_class = PostSerilizer

#!  class PostDestroyAPIView(generics.DestroyAPIView):
#!      queryset = Post.objects.all()
#!      serializer_class = PostSerilizer

#!  class PostDetailAPIView(generics.RetrieveAPIView):
#!      queryset = Post.objects.all()
#!      serializer_class = PostSerilizer

    
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerilizer
    permission_classes = [IsAuthenticatedOrReadOnly,]