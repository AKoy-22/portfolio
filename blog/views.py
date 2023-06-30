from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import FormView, CreateView
from django.http import HttpResponseRedirect
from django.urls import reverse
#from datetime import date
from .models import Post, Comment
from .forms import CommentForm
# dummy data for the posts



# def get_date(post):
#     return post['date']  # or post.get('date')

# print(get_date(posts))
# print(posts[0]['date'])

# Create your views here

class AboutView(View):
    def get(self, request):
        return render(request, "blog/about-me.html")


class StartingView(ListView):
    template_name = "blog/index.html"
    model = Post 
    ordering = ["-date", "-title"]
    #context_object_name = "posts"

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query[:3] 
        return data 

""""
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
"""

class PostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    #context_object_name = "all_posts"

"""
def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts  # all_posts list of dictionary is passed to all-posts.html
    })
"""

class PostDetailView(View):
    model = Post 
    def get(self, request, slug):
        post = Post.objects.get(slug=slug) 
        stored_posts = request.session.get("stored_posts")
        has_read_later = True
        if stored_posts is None or len(stored_posts) == 0:
            has_read_later = False
        elif int(post.id) not in stored_posts:
            has_read_later = False
        elif int(post.id) in stored_posts:
            has_read_later = True

        return render(request, "blog/post-detail.html",{
            "post":post,
            "comment_form":CommentForm(),
            "comments":post.comments.all().order_by("-id"),
            "has_read_later":has_read_later
        })
        
    
    #template_name = "blog/post-detail.html"
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["comment_form"] = CommentForm() #set up the form 
    #     return context
    
    def post(self, request, slug):
        post = Post.objects.get(slug=slug)   
        comment_form= CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False) #because post field in comment table was excluded 
            comment.post = post  #manually add which post it relates to
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page", args=[slug])) #send get reqeuest to the same page
        else:
            return render(request, "blog/post-detail.html", {
            "post":post,
            "comment_form":comment_form,
             "comments":post.comments.all().order_by("-id")
        })
    
    #context_object_name = "selected_post"
    #can automatically search for data by id/pk or slug
    #also raise 404 error automatically



"""
def post_detail(request, slug):
    # finds next element matching certain condition
    #identified_post = next(post for post in all_posts if post['slug'] == slug)

    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post,
        "post_tags": identified_post.tag.all()
    })  # accepts slug parameter
"""

class ReadLaterView(View):
    def getData(self, request):
        stored_posts = request.session.get("stored_posts")
        context = {}
        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            read_later = Post.objects.filter(id__in=stored_posts)
            context["posts"]=read_later
            context["has_posts"]=True
        return context
    
    def get(self, request):
        stored_posts = request.session.get("stored_posts")
        context = {}
        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            read_later = Post.objects.filter(id__in=stored_posts)
            context["posts"]=read_later
            context["has_posts"]=True
        return render(request, "blog/stored-posts.html", context)

    def post(self, request):
        context = self.getData(self.request)
        stored_posts = request.session.get("stored_posts")
        if "remove_id" in request.POST:
            post_id=int(request.POST["remove_id"])
            print("debug here stored_posts" + str(stored_posts))
            print("debug here post_id" + str(post_id))
            stored_posts.remove(post_id)
            request.session["stored_posts"] = stored_posts
            
            return HttpResponseRedirect(reverse("read-later"))  #render(request, "blog/stored-posts.html", context)
        else:
            if stored_posts is None:
                stored_posts=[] #set it to empty list if there is no session 
            post_id= int(request.POST["post_id"])
            if post_id not in stored_posts:
                stored_posts.append(post_id) 
                request.session["stored_posts"] = stored_posts #session is created if did not exit, update if existed 
            return HttpResponseRedirect(reverse("read-later"))


