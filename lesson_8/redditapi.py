1. Make an account on Reddit & 
2. import praw
3. ipython : pip install praw

______________

4. create new notebook -> import praw

api = praw.Reddit(
	CLIENT_ID = 
	CLIENT_SECRET = 
	USER_AGENT =
)
https://www.reddit.com/r/askreddit

api.read_only

in Jupiter Notebook [*] means loading..

______________

subreddit("askreddit") = the category / subject where you want to load your api from
.hot(limit = 10) = the amount of messages you want to get/show
