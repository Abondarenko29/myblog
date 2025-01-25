from django.shortcuts import render
from .models import Post, Author


# Create your views here.
def all(request):
    posts = Post.objects.all().order_by("-published_date").values()
    context = {"posts": posts}
    return render(request,
                  'blog/post_list.html',
                  context=context)


def post(request, id):
    post = Post.objects.get(id=id)
    context = {
               "post": post,
               "delta_days": post.published_recently()
               }
    return render(request,
                  "blog/post_details.html",
                  context)


def author_posts(request, id):
    author = Author.objects.get(id=id)
    context = {
        "author_posts": author.posts.all()
    }
    return render(request,
                  "blog/author_posts.html",
                  context)
