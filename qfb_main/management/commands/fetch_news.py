from django.core.management.base import BaseCommand
from qfb_main.models import Post
import requests
from django.conf import settings
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Fetch news from API and archive old articles'

    def handle(self, *args, **kwargs):
        # Archive current articles
        Post.objects.filter(category='Tech', is_archived=False).update(is_archived=True)

        # Fetch new articles
        url = f"https://newsdata.io/api/1/news?apikey={settings.NEWS_API_KEY}"
        response = requests.get(url)
        data = response.json()

        print(f"API Response: {data}")  # Debugging line to check what data contains

        if response.status_code == 200:
            for article in data.get('articles', []):
                author, created = User.objects.get_or_create(username=article['source']['name'])
                Post.objects.create(
                    title=article['title'],
                    content=article['description'],
                    author=author,
                    status=1,
                    is_archived=False  # New articles are not archived
                )
        else:
            print(f"Failed to fetch news: {response.status_code}")
            print(f"Error details: {response.text}")  # Print the full response body for debugging
