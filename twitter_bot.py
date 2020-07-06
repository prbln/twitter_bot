import tweepy

auth = tweepy.OAuthHandler('AnvapSplNBn2e02gcyrh1RTl0', '1UzCLwgByKn129xkcIPrhzkRFFH4Xhuxb6e3aeh4Any4Cmxpjo')
auth.set_access_token('1278306228188246016-axw2Ymq8Y2lNI49bhXUiJJCokNlNrW', '8StFu27muDU0b2q417pFyOWlxBgYlrsOVVmscdB8P4bZX')
api = tweepy.API(auth)
search_string = 'depression'
no_of_tweets = 5

for tweet in tweepy.Cursor(api.search,search_string).items(no_of_tweets):
	try:
		while True:
			tweet.favorite()
			print('Do you need help?')
	except tweepy.TweepError as e:
		print(e.reason)
	except tweepy.RateLimitError:
		time.sleep(300)
	except StopIteration:
		break

