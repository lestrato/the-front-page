from django import template
import time
import re
import ast

register = template.Library()
from HTMLParser import HTMLParser

@register.filter
def parse_media(post):
    ''' post file '''
    # safely evaluate the expression node: post
    post = ast.literal_eval(post)

    parser = HTMLParser()
    url = post.get('url', None)
    domain = post.get('domain', None)

    selftext_html = post.get('selftext_html', '')

    # if there's embedabble media
    if post.get('media_embed').get('content', None):
        html_decoded_string = parser.unescape(post.get('media_embed').get('content'))
        return html_decoded_string

    # check for self_text
    if selftext_html != None:
        # print selftext_html
        html_decoded_string = parser.unescape(selftext_html)
        return "<div id='post_text_container'>"+html_decoded_string+"</div>"

    #gifv
    # story_data = story_data.get('url', '')
    if re.match('.*\.gifv', url):
        url = url[:-4]+'mp4'
        # return '<video muted="" loop="" poster="" controls="controls"><source src="'+url+'" type="video/gifv"></video>'
        return '<video controls="controls"><source src="'+url+'" type="video/mp4"></video>'

    # mp4
    if re.match('.*\.mp4', url):
        return '<video controls="controls"><source src="'+url+'" type="video/mp4"></video>'

    # if gfycat, add giant and .mp4:

    # webm
    if re.match('.*\.webm', url):
        return '<video ><source src="'+url+'" type="video/webm"</video>'



    # regular images (redditupload)
    if domain == 'i.reddituploads.com':
        return '<img src="'+url+'">'

    # albums
    # story_data = story_data.get('secure_media_embed', '')

    # .jpeg, .jpg, .png, .gif, .bmp
    if re.match('.*\.jpeg', url) or re.match('.*\.jpg', url) or re.match('.*\.png', url) or re.match('.*\.gif', url) or re.match('.*\.bmp', url):
        return '<img src="'+url+'">'# <img src=""

    # catch non-imgur links
    if re.match('.*imgur\.com.*', url) and not re.match('.*imgur\.com\/gallery\/.*', url):
        return '<img src="'+url+'.jpg">'

    return None
