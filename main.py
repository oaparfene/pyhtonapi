import tweepy
from config import consumer_key, consumer_secret, access_token, access_token_secret

# Authenticate with the Twitter API using the keys and secrets
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Fetch the recent mentions of the account
mentions = api.mentions_timeline()

# Print the text of the mentions
for mention in mentions:
    print(mention.text)



def main():
    masterHandle = input("Please enter your twitter handle:\n")
    masterUserlist = api.GetUsersSearch(masterHandle,1,10)
    print(masterUserlist)

#main()


