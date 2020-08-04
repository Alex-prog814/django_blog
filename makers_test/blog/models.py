from django.db import models
from django.contrib.auth import get_user_model
#uzhe pishem kod

class Category(models.Model):               #vse modeli django nasleduyutsya ot models.Model
    name = models.CharField(max_length=50, unique=True)          #vmesto varchar, v django ispol'zuem Charfield
    slug = models.SlugField(max_length=50, primary_key=True) #pervichnyi klyuch

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')           #privyazali Category 
    text = models.TextField()     #kak Charfield, no bez ogranichenii
    creation_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(null=True, blank=True, upload_to='posts')     #v bd popadayut ssylki na kartinki, sami kartinki hranyatsya na servake

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('post-details', args=[str(self.id)])