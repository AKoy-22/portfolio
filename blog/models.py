from django.db import models
from django.core.validators import MinLengthValidator
from django.urls import reverse

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=150)
    #image_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images', null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True)  # db_index=True is set automatically
    content = models.TextField(validators=[MinLengthValidator(10)])
    # so that we don't need to do posts_set
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True) # related_name="posts",
    tag = models.ManyToManyField(Tag)
    
    def __str__(self):
        return f"{self.title} {self.date}"

    def get_absolute_url(self):
        return reverse("post-detail-page", args=[self.slug])
    

class Comment(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField(max_length=254)
    user_comment = models.TextField(validators=[MinLengthValidator(10)])
    date = models.DateField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return f"{self.user_name} {self.user_email}"
