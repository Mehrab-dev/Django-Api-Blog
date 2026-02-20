from rest_framework import serializers

from django.urls import reverse

from blog.models import Post , Category
from account.models import User

class PostSerializer(serializers.ModelSerializer) :
    snippet = serializers.ReadOnlyField(source="get_snippet")
    absolute_url = serializers.SerializerMethodField(method_name="get_absolute_url")
    relative_url = serializers.URLField(source="get_relative_url")
    category = serializers.SlugRelatedField(many=False,slug_field="name",queryset=Category.objects.all())
    author = serializers.SlugRelatedField(many=False,slug_field="email",queryset=User.objects.all())

    class Meta :
        model = Post
        fields = ["id","relative_url","absolute_url","title","content","snippet","author","category","status","published_date"]
        read_only_fields = ["id"]

    def get_absolute_url(self,object) :
        request = self.context.get("request")
        url = reverse("blog:api_v1:post_detail_modelviewsets",kwargs={"pk":object.pk})
        return request.build_absolute_uri(url)
    
    def to_representation(self, instance):
        request = self.context.get("request")
        rep = super().to_representation(instance)
        if request.parser_context.get("kwargs").get("pk") :
            rep.pop("absolute_url",None)
            rep.pop("snippet",None)
        else :
            rep.pop("content",None)
            rep.pop("relative_url",None)
        return rep


class CategorySerializer(serializers.ModelSerializer) :

    class Meta :
        model = Category
        fields = ["id","name","created_date"] 