from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)



class Profile(BaseModel):
    name = models.CharField(max_length=100)
    image = models.ImageField("Profile/")
    description = models.TextField()


class Social_link(BaseModel):
    name = models.CharField(max_length=110)
    icon = models.CharField(max_length=110)
    url = models.CharField(max_length=110)
    order = models.PositiveIntegerField()


class Post(BaseModel):
    title = models.CharField(max_length=120)
    image = models.ImageField("image/")
    description = models.TextField()
    body = models.TextField()



class About(BaseModel):
    body = models.TextField()