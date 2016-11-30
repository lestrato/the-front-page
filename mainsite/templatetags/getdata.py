from django import template
import time
import ast

register = template.Library()

@register.filter
def get_data(post, json):
    post = ast.literal_eval(post)

    if json == 'title':
        data = post.get(json, '')
    elif json == 'score':
        data = post.get(json, 0)
    elif json == 'url':
        data = post.get(json, '')
    elif json == 'subreddit':
        data = post.get(json, '')
    elif json == 'media_embed':
        data = post.get(json, '')
    elif json == 'over_18':
        data = post.get(json, '')
    elif json == 'gilded':
        data = post.get(json, '')
    elif json == 'num_comments':
        data = post.get(json, 0)
    elif json == 'permalink':
        data = post.get(json, '')
    elif json == 'domain':
        data = post.get(json, '')
    elif json == 'selftext':
        data = post.get(json, '')
    elif json == 'post_hint':
        data = post.get(json, '')

    return data
