from rest_framework.test import APIClient
import pytest

from django.urls import reverse
from datetime import datetime

from account.models import User
from blog.models import Category,Post


@pytest.fixture
def common_user() :
    user_obj = User.objects.create_user(email="programmer.py.mail@gmail.com",password="Mm20399990")
    return user_obj

@pytest.fixture
def category_obj() :
    cat = Category.objects.create(name="IT")
    return cat

@pytest.mark.django_db
class TestPostApi:

    def test_blog_get_post_response_200(self,common_user) :
        client = APIClient()
        user = common_user
        client.force_authenticate(user=user)
        url = reverse("blog:api_v1:post_modelviewsets")
        response = client.get(url)

        assert response.status_code == 200

    def test_blog_create_post_response_401(self,common_user,category_obj) :
        client = APIClient()
        # user = common_user
        # category = category_obj
        url = reverse("blog:api_v1:post_modelviewsets")
        data = {
            "title" : "test",
            "content" : "description",
            "author" : common_user,
            "category" : category_obj,
            "status" : True,
            "published_date" : datetime.now()
        }
        response = client.post(url,data)

        assert response.status_code == 401
    
    def test_blog_create_post_response_201(self,common_user,category_obj) :
        client = APIClient()
        client.force_authenticate(user=common_user)
        data = {
            "title" : "test",
            "content" : "description",
            "author" : common_user,
            "category" : category_obj,
            "status" : True,
            "published_date" : datetime.now()
        }
        url = reverse("blog:api_v1:post_modelviewsets")
        response = client.post(url,data)

        assert response.status_code == 201

    def test_blog_create_post_invalid_data_and_response_400(self,common_user) :
        client = APIClient()
        client.force_authenticate(user=common_user)
        data = {
            "title" : "test",
            "published_date" : datetime.now()
        }
        url = reverse("blog:api_v1:post_modelviewsets")
        response = client.post(url,data)

        assert response.status_code == 400