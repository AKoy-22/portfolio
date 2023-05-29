from django.shortcuts import render, get_object_or_404
#from datetime import date
from .models import Post
# dummy data for the posts


def get_date(post):
    return post['date']  # or post.get('date')

# print(get_date(posts))
# print(posts[0]['date'])

# Create your views here


def starting_page(request):
    # get the latest posts
    # sort by date and returns a new list. if all_posts.sort(key) original list gets sorted
    latest_posts = Post.objects.all().order_by("-date")[:3]  #- makes it desc. django will convert this into sql so only the first 3 are fetched.
    #cannot do [:-3] it is not supportd
    #sorted_posts = sorted(all_posts, key=get_date)
    #latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
        # latest_posts can be used in index.html
    })


def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts  # all_posts list of dictionary is passed to all-posts.html
    })


def post_detail(request, slug):
    # finds next element matching certain condition
    #identified_post = next(post for post in all_posts if post['slug'] == slug)

    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post,
        "post_tags": identified_post.tag.all()
    })  # accepts slug parameter
