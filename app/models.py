from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)



class Profile(BaseModel):
    name = models.CharField(max_length=100)
    image = models.ImageField(max_length=110)
