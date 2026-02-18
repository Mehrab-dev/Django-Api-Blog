from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("index/",views.IndexView.as_view(),name="index"),
    path("redirect/",views.RedirectViews.as_view(),name="redirect"),
    path("post/list/",views.PostListView.as_view(),name="post_list"),
    path("post/<int:pk>/",views.PostDetailView.as_view(),name="post_detail"),
    path("post/create/",views.PostCreateView.as_view(),name="post_create"),
    path("post/update/<int:pk>/",views.PostUpdateView.as_view(),name="post_update"),
    path("post/delete/<int:pk>/",views.PostDeleteView.as_view(),name="post_delete"),

]