from django.shortcuts import render
from django.views import generic
from qfb_main.models import Post
import requests
from django.conf import settings
from django.contrib.auth.models import User

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.fetch_news()
        return context

    @staticmethod
    def fetch_news():
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={settings.NEWS_API_KEY}"
        response = requests.get(url)
        data = response.json()

        for article in data['articles']:
            # Create or get a user object for the news media source
            author, created = User.objects.get_or_create(username=article['source']['name'])
            
            Post.objects.create(
                title=article['title'],
                content=article['description'],
                author=author,  # Set to the news media source
                status=1  # Published
            )
