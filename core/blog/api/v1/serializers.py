from rest_framework import serializers

from blog.models import Post

class PostSerializer(serializers.ModelSerializer) :

    class Meta :
        model = Post
        fields = ["id","title","content","author","category","status","published_date"]
        read_only_fields = ["id"]