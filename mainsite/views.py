from django.shortcuts import render

from mainsite.crawler import fetch_reddit_posts
from mainsite.models import RedditJson, RedditPost

from django.utils import timezone
from requests import ConnectionError

def index(request):

    def fetch_new_posts():
        """
        Fetch new posts from Reddit's API
        """
        try: # fetch new json
            return fetch_reddit_posts()
        except (ConnectionError, KeyError) as err:
            return None

    def get_old_posts():
        """
        Fetch and interpret stored posts from database
        """
        all_posts = {}
        for entry in RedditPost.objects.all():
            if entry.subreddit in all_posts:
                all_posts[entry.subreddit] += [entry.content]
            else:
                all_posts[entry.subreddit] = [entry.content]
        return all_posts

    def replace_posts():
        """
        Cleanse the database of all posts
        Set last_fetched to nowtime
        Interpret the dictionary of all posts:
            - separate the keys into different subreddits
            - insert the subreddit, content tuple into the table
        """
        print 'STATUS: replacing old posts'
        RedditPost.objects.all().delete()
        old_json.last_fetched = timezone.now()
        old_json.save()
        for category in all_posts:
            for post in all_posts[category]:
                new_post = RedditPost(
                    subreddit=category,
                    content=post,
                )
                new_post.save()

    old_json = RedditJson.objects.first()
    # error = None

    if not old_json:
        """
        Check if there's information in the RedditPost table
        """
        print 'STATUS: old json doesn\'t exist -- creating new json'
        old_json = RedditJson() # create new json object with timezone.now()
        old_json.save()
        all_posts = fetch_new_posts()
        if all_posts:
            replace_posts()

    elif (timezone.now() - old_json.last_fetched).seconds > 600:
        """
        Check if the JSON in the RedditPost table expired by checking RedditJSON
        last_fetched
        """
        print 'STATUS: old json expired'
        all_posts = fetch_new_posts()
        if all_posts:
            replace_posts()

    """
    Now, the JSON exists in table.
    """
    print 'STATUS: json exists in table'
    all_posts = get_old_posts()

    last_fetched_difference = ((timezone.now() - old_json.last_fetched).seconds)


    return render(request, 'index.html', {
        'all_posts' : all_posts,
        'last_fetched_difference' : last_fetched_difference,
    })
