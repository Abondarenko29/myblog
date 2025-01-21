from django.shortcuts import render
from .models import Post


# Create your views here.
def all(request):
    posts = Post.objects.all().order_by("-published_date").values()
    context = {"posts": posts}
    return render(request,
                  'blog/post_list.html',
                  context=context)
