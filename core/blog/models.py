from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class Post(models.Model) :
    title = models.CharField(max_length=55)
    content = models.TextField(blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey("Category",on_delete=models.SET_NULL,null=True)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    def __str__(self) :
        return self.title
    
    def get_snippet(self) :
        return self.content[:10] + "....."
    
    def get_relative_url(self) :
        return reverse("blog:api_v1:post_detail_modelviewsets",kwargs={"pk":self.id})

class Category(models.Model) :
    name = models.CharField(max_length=55)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.name