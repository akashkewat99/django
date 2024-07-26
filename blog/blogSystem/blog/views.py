from django.views.generic import ListView,CreateView
from .models import Post

class PostList(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'


class PostCreate(CreateView):
    model = Post
    template_name = 'blog/postcreate.html'
    fields = ['title','content']
    success_url = '/blogs/list/'
    