from __future__ import unicode_literals

from django.db import models
from datetime import datetime

class RedditJson(models.Model):
    last_fetched = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = 'redditjson'

    # def __str__(self):
    #     return self.last_fetched

class RedditPost(models.Model):
    subreddit = models.CharField(max_length=20)
    content = models.TextField()

    class Meta:
        db_table = 'redditpost'

    def __str__(self):
        return self.content
