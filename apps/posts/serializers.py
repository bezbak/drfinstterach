from rest_framework import serializers
from apps.posts.models import Post

class PostSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','image_or_video','description','owner', 'created', 'user_info') #!"__all__" 

    user_info = serializers.SerializerMethodField()
    def get_user_info(self, obj):
        qs = obj.owner
        data = {}
        data.setdefault('id',qs.id)
        data.setdefault('username',qs.username)
        if qs.profile_image:
            data.setdefault('profile_image',qs.profile_image)
        else:
            data.setdefault('profile_image','')
        return data
#! Настройки api