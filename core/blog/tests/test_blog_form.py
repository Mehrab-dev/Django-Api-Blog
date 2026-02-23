# from django.test import TestCase

# from datetime import datetime

# from account.models import User
# from blog.models import Category
# from blog.forms import PostForm

# class TestForm(TestCase) :

#     def test_post_form_valid_date(self) :
#         user = User.objects.create_user(email="programmer.py.mail@gmail.com",password="Mm20399990")
#         category = Category.objects.create(name="IT")
#         form = PostForm(data ={
#             "title" : "test",
#             "content" : "description",
#             "author" : user,
#             "category" : category,
#             "status" : True,
#             "published_date" : datetime.now()
#         })

#         self.assertTrue(form.is_valid())
    
#     def test_post_form_invalid_data(self) :
#         form = PostForm(data = {
#             "title" : "test",
#             "status" : True,
#             "published_date" : datetime.now()
#         })

#         self.assertFalse(form.is_valid())