# from django.test import TestCase

# from datetime import datetime

# from blog.models import Post,Category
# from account.models import User


# class TestModel(TestCase) :

#     def test_create_post_with_valid_data(self) :
#         user = User.objects.create_user(email="programmer.py.mail@gmail.com",password="Mm20399990")
#         category = Category.objects.create(name="IT")
#         post = Post.objects.create(
#             title = "test",
#             content = "description",
#             author = user,
#             category = category,
#             status = True,
#             published_date = datetime.now()
#         )

#         self.assertTrue(Post.objects.filter(pk=post.id).exists())
#         self.assertEqual(post.title,"test")