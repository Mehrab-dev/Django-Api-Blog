from django.test import TestCase
from django.urls import reverse , resolve

from blog.views import  IndexView , PostDetailView

class TestUrl(TestCase) :

    def test_blog_index_url_resolve(self) :
        url = reverse("blog:index")
        self.assertEqual(resolve(url).func.view_class,IndexView)

    def test_blog_post_detail_url_resolve(self) :
        url = reverse("blog:post_detail",kwargs={"pk":1})
        self.assertEqual(resolve(url).func.view_class,PostDetailView)
