from rest_framework import serializers
from apps.posts.models import Post

class PostSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"