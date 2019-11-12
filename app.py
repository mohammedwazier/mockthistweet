import sys
import tweepy
import time
import os
from kalimat import Kalimat
from generator import drawText
from auth import authentication
from load import loadData, writeData

auth = authentication()

fileMeme = 'img/meme_final.png'
triggeringWords = ["please", "mock", "pls"]

FILE_LAST_ID = os.getenv("FILE_LAST_ID")


def getMentionTweet(keywords, since_id):
    api = tweepy.API(auth)
    new_since_id = since_id

    for tweet in tweepy.Cursor(api.mentions_timeline, since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)

        words = tweet.text.split()

        for tw in triggeringWords:
            if tw in words:
                tweet_target = api.get_status(tweet.in_reply_to_status_id)
                k = Kalimat(tweet_target.text)
                textNormal = k.getSentence()
                textTransformed = k.transform()
                drawText(textNormal, textTransformed, "img/meme_squared.png")
                time.sleep(15)
                api.update_with_media(
                    fileMeme,
                    status=textTransformed,
                    in_reply_to_status_id=tweet.id,
                    auto_populate_reply_metadata=True)

    return new_since_id


while True:
    last_id = loadData(FILE_LAST_ID)
    last_id = int(last_id[-1])
    since_id = getMentionTweet(triggeringWords, last_id)
    print(since_id, last_id)
    if (last_id != since_id):
        writeData(FILE_LAST_ID, str(since_id))
    else:
        print('not posting and writing')
    for sec in range(300, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} second to check mention.\r".format(sec))
        sys.stdout.flush()
        time.sleep(1)
