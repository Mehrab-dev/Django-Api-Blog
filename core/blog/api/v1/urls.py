from django.urls import path

from . import views

app_name = "ali_v1"

urlpatterns = [
    # path("posts/",views.post_list_api,name="post_list"),
    # path("posts/<int:pk>/",views.post_detail_api,name="post_detail"),

    # APIView
    # path("posts/",views.PostListApi.as_view(),name="post_list"),
    # path("posts/<int:pk>/",views.PostDetailApi.as_view(),name="post_detail"),

    # GenericsAPIView
    # path("posts/",views.PostListApi.as_view(),name="post_list"),
    # path("posts/<int:pk>/",views.PostDetailApi.as_view(),name="post_detail"),

    # mixins
    # path("posts/",views.PostListApi.as_view(),name="post_list"),
    # path("posts/<int:pk>/",views.PostDetailApi.as_view(),name="post_detail"),

    # viewsets and modelviewsets
    # path("posts/",views.PostViewSets.as_view({"get":"list","post":"create"}),name="post_list_viewsets"),
    # path("posts/<int:pk>/",views.PostViewSets.as_view({"get":"retrieve","put":"update","delete":"destroy"}),name="post_detail_viewsets"),

    path("posts/",views.PostModelViewSets.as_view({"get":"list","post":"create"}),name="post_modelviewsets"),
    path("posts/<int:pk>/",views.PostModelViewSets.as_view({"get":"retrieve","put":"update","delete":"destroy"}),name="post_modelviewsets"),
]