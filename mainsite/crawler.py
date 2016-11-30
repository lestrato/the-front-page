import requests
from bs4 import BeautifulSoup

def fetch_reddit_posts():
    news = []
    community = []
    media = []
    art = []
    funny = []
    gaming = []

    # def get_stories_from_url(url):


    headers = { 'user-agent': 'the front page/0.0.1' }
    url = 'https://www.reddit.com/r/news+worldnews+upliftingnews+funny+programmerhumor+jokes+blackpeopletwitter+gaming+leagueoflegends+hearthstone+askreddit+iama+tifu+videos+gifs+pics+movies+art+music+listentothis/.json?limit=75'
    #
    # if subreddit_name == None:
    #     r = requests.get(url, headers)
    # else:
    #     r = requests.get('https://www.reddit.com/r/'+subreddit_name+'.json', headers)

    r = requests.get(url, headers)
    result = r.json()
    stories = result['data']['children']

    for story in stories:
        story_data = story['data']
        story_subreddit = story_data.get('subreddit', '').encode('utf-8').lower()
        if story_subreddit == 'news' or story_subreddit == 'upliftingnews' or story_subreddit == 'worldnews':
            news.append(story_data)
        if story_subreddit == 'askreddit' or story_subreddit == 'iama' or story_subreddit == 'tifu':
            community.append(story_data)
        if story_subreddit == 'videos' or story_subreddit == 'pics' or story_subreddit == 'gifs':
            media.append(story_data)
        if story_subreddit == 'movies' or story_subreddit == 'art' or story_subreddit == 'music' or story_subreddit == 'listentothis':
            art.append(story_data)
        if story_subreddit == 'funny' or story_subreddit == 'programmerhumor' or story_subreddit == 'jokes' or story_subreddit == 'blackpeopletwitter':
            funny.append(story_data)
        if story_subreddit == 'gaming' or story_subreddit == 'leagueoflegends' or story_subreddit == 'hearthstone':
            gaming.append(story_data)

    return {'news':news, 'community':community, 'media':media, 'art':art, 'funny':funny, 'gaming':gaming}


    # count = 25

#
