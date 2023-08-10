from django.urls import path
from apps.posts.views import PostAPIView, PostCreateAPIView


urlpatterns = [
    path('', PostAPIView.as_view()),
    path('create/', PostCreateAPIView.as_view()),
]
