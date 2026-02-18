from django.views.generic.base import TemplateView , RedirectView
from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView

from blog.models import Post
from .forms import PostForm

class IndexView(TemplateView) :
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        content = super().get_context_data(**kwargs)
        content["name"] = "Mehrab"
        return content

class RedirectViews(RedirectView) :
    url = "https://maktabkhooneh.org/"

class PostListView(ListView) :
    # model = Post
    # queryset = Post.objects.filter(status=True)
    context_object_name = "post"

    def get_queryset(self):
        posts = Post.objects.filter(status=True)
        return posts

class PostDetailView(DetailView) :
    model = Post
    context_object_name = "post"

class PostCreateView(CreateView) :
    model = Post
    form_class = PostForm
    success_url = "/blog/post/list/"

class PostUpdateView(UpdateView) :
    model = Post
    form_class = PostForm
    success_url = "/blog/post/list/"

class PostDeleteView(DeleteView) :
    model = Post
    success_url = "/blog/post/list/"
    context_object_name = "post"