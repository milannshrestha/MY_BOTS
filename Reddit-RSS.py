import feedparser
from time import sleep
from discord_webhook import DiscordWebhook
url = ('webhook')

parse = feedparser.parse('https://www.reddit.com/r/<subreddit>.rss')

while True:
        for post in parse.entries:
                xx = (post.link)
                webhook = DiscordWebhook(url=url, content=xx)
                response = webhook.execute()
                sleep(10)

