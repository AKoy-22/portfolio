from django.urls import path
from .import views
urlpatterns = [
    path("", views.StartingView.as_view(), name="starting-page"),
    path("posts", views.PostsView.as_view(), name="posts-page"),
    path("posts/<slug:slug>", views.PostDetailView.as_view(), name="post-detail-page"),
    path("read-later", views.ReadLaterView.as_view(), name="read-later"),
    path("about", views.AboutView.as_view(), name="about-me"),
    path("skills", views.SkillsView.as_view(), name="my-skills"),
]
