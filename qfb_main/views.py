from django.shortcuts import render
from django.views import generic
from qfb_main.models import Post  # Make sure to update your Post model to include 'is_archived' fields
import requests
from django.conf import settings
from django.contrib.auth.models import User

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1, is_archived=False).order_by("-created_on")  # Updated to exclude archived posts
    template_name = "index.html"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def fetch_news():
    # Archive current articles in "Latest News" category
    Post.objects.filter(category='Latest News', is_archived=False).update(is_archived=True)

    # Fetch new articles
    url = f"https://newsapi.org/v2/everything?q=Apple&from=2023-09-19&sortBy=popularity&apiKey={settings.NEWS_API_KEY}"
    response = requests.get(url)
    data = response.json()

    for article in data['articles']:
        author, created = User.objects.get_or_create(username=article['source']['name'])
        Post.objects.create(
            title=article['title'],
            content=article['description'],
            author=author,
            status=1,
            category='Latest News',  
            is_archived=False  
        )
