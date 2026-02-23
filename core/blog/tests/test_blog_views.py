# from django.test import TestCase,Client
# from django.urls import reverse

# from datetime import datetime

# from blog.models import Post,Category
# from account.models import User


# class TestView(TestCase) :
#     def setUp(self) : 
#         self.client = Client()

#         self.user = User.objects.create_user(email="programmer.py.mail@gmail.com",password="Mm20399990")
#         self.category = Category.objects.create(name="IT")
#         self.post = Post.objects.create(
#             title = "test",
#             content = "description",
#             author = self.user,
#             category = self.category,
#             status = True,
#             published_date = datetime.now()
#         )

#     def test_blog_index_url_response_200(self) :
#         url = reverse("blog:index")
#         response = self.client.get(url)

#         self.assertIn("Mehrab",response.content.decode())
#         self.assertEqual(response.status_code,200)
#         self.assertTemplateUsed(template_name="indexasdasd.html")  # can not be checke!
    
#     def test_blog_post_detail_url_reponse_302(self) :
#         url = reverse("blog:post_detail",kwargs={"pk":self.post.id})
#         response = self.client.get(url)

#         self.assertEqual(response.status_code,302)
        
#     def test_post_detail_logged_in_response(self) :
#         self.user.is_active = True
#         self.user.save()
#         self.client.force_login(self.user)
#         url = reverse("blog:post_detail",kwargs={"pk":self.post.id})
#         response = self.client.get(url)

#         self.assertEqual(response.status_code,200)