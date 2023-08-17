
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from apps.posts.views import PostViewSet
from apps.users.views import UserViewSet
from django.views.generic import RedirectView

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'users', UserViewSet)
api_urlpatterns = [
    path('posts/', include('apps.posts.urls')),
    path('users/', include('apps.users.urls')),
    path('chat/', include('apps.chat.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urlpatterns)),
    path('api/', include(router.urls)),
    path('', RedirectView.as_view(url='/api/'))
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)