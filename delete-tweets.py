import tweepy

# import requests
# import os

# secrets_file = open('secrets.txt', 'r')
# key = "hpxonaJMJrf5RGvhe6Q4MFK24"
# key_secret = "IOr0ZYmUkoOmMsck8mUUAnlU8SsV3PWXPN53jffSevT1xHqHAb"
# access = "1202465097542619136-Xi5cMa09j9xuICkMf4m91DJpsqO1sQ"
# access_secret = "3p4iDwA4Fs0VSaozNwHNVlJat98hr77uWRaeLaOKH5Jln"

with open('secrets.txt', 'r') as secrets_file:
    key = secrets_file.readline().strip()
    key_secret = secrets_file.readline().strip()
    access = secrets_file.readline().strip()
    access_secret = secrets_file.readline().strip()


auth = tweepy.OAuthHandler(key, key_secret)
auth.set_access_token(access, access_secret)
api = tweepy.API(auth)
print()
print(key, key_secret, access, access_secret)
print('If you have a lot of tweets, this WILL take a while to complete, including an optional review process that will'
      'result in your tweets being iterated over twice.')


def delete_tweets_by_text():
    tweet_array = []
    print()
    delete_phrase = input('Please enter a phrase that you wish to purge from your Twitter account: ')
    print('Finding tweets...')
    for tweet in tweepy.Cursor(api.user_timeline).items():
        if delete_phrase.lower() in tweet.text.lower():
            print(tweet.text, "@", tweet.created_at)
            tweet_array.append(tweet)

    choice = input(f'There are {len(tweet_array)} tweets that will be deleted, do you wish to proceed? (y/n)')

    if choice == 'y':
        print('Deleting tweets...')
        for tweet in tweet_array:
            api.destroy_status(tweet.id)
            print(f'Deleted status id: {tweet.id}')


while True:
    delete_tweets_by_text()
