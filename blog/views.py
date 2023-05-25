from django.shortcuts import render
from datetime import date
# dummy data for the posts
all_posts = [
    {
        "slug":"hike-in-the-mountains",
        "image": "mountains.jpg",
        "author":"akiko",
        "date": date(2021, 7,21),
        "title":"Mountain Hiking",
        "excerpt":"THere is nothing like the view you ge twhen you .........",
        "content":""" 
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolorum est placeat quibusdam 
            quam exercitationem ullam aspernatur perspiciatis, 
            laboriosam magnam. Est deleniti at labore architecto inventore id quos minima ut dolores!

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolorum est placeat quibusdam 
            quam exercitationem ullam aspernatur perspiciatis, 
            laboriosam magnam. Est deleniti at labore architecto inventore id quos minima ut dolores
        """
    },
        {
        "slug":"in-to-the-woods",
        "image": "woods.jpg",
        "author":"akiko",
        "date": date(2022, 5,21),
        "title":"Into the Woods!!!",
        "excerpt":"Into the woods woods woods !!!  THere is nothing like the view you ge twhen you get to the woods .........",
        "content":""" 
           Into the woods woods woods !!! amet consectetur adipisicing elit. Dolorum est placeat quibusdam 
            quam exercitationem ullam aspernatur perspiciatis, 
            laboriosam magnam. Est deleniti at labore architecto inventore id quos minima ut dolores!

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolorum est placeat quibusdam 
            quam exercitationem ullam aspernatur perspiciatis, 
            laboriosam magnam. Est deleniti at labore architecto inventore id quos minima ut dolores
        """
    },
    {
        "slug":"programming-is-fun",
        "image": "coding.jpg",
        "author":"akiko",
        "date": date(2023, 4,21),
        "title":"Programming is Fun",
        "excerpt":"Programming is fun fun fun.nothing like the view you ge twhen you get to the woods .........",
        "content":""" 
            programming is.....Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolorum est placeat quibusdam 
            quam exercitationem ullam aspernatur perspiciatis, 
            laboriosam magnam. Est deleniti at labore architecto inventore id quos minima ut dolores!

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolorum est placeat quibusdam 
            quam exercitationem ullam aspernatur perspiciatis, 
            laboriosam magnam. Est deleniti at labore architecto inventore id quos minima ut dolores
        """
    },
]

def get_date(post):
    return post['date'] # or post.get('date')

#print(get_date(posts))
#print(posts[0]['date'])

# Create your views here

def starting_page(request):
    #get the latest posts 
    sorted_posts = sorted(all_posts, key=get_date) #sort by date and returns a new list. if all_posts.sort(key) original list gets sorted
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts":latest_posts
        #latest_posts can be used in index.html
    })


def posts(request):

    return render(request,"blog/all-posts.html",{
        "all_posts":all_posts  #all_posts list of dictionary is passed to all-posts.html 
    } )


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug']==slug)#finds next element matching certain condition
    return render(request, "blog/post-detail.html", {
        "post":identified_post
    }) #accepts slug parameter 
