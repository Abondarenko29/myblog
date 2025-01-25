from django.urls import path
import blog.views as views

urlpatterns = [
    path("", views.all, name="all"),
    path("<int:id>", views.post, name="post-details"),
    path("author/<int:id>", views.author_posts, name="author-posts"),
]
