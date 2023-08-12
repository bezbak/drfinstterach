from django.db import models
from apps.users.models import User
# Create your models here.
class Post(models.Model):
    image_or_video = models.FileField(
        upload_to='posts_files/'
    )
    description = models.TextField()
    owner = models.ForeignKey(
        User,
        related_name='posts',
        on_delete=models.CASCADE
    )
    created = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.description[:10]}"
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'