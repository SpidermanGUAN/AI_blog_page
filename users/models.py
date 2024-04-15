from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="django_project/static/blog/testimg.png", upload_to="profile_pics")

    def __str__(self):
        return f"{self.user.username} Profile"
    
    def get_user_posts(self):
        return self.user.post_set.all()
