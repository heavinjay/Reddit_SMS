import praw
import time
import schedule
import SMS
import cred

# main app function
def myapp():
    # for reddit api
    reddit = praw.Reddit(client_id=cred.keyring.get_password('client_ID', 'reddit_clientID'),
                         client_secret=cred.keyring.get_password('client_pass', 'reddit_clientPass'),
                         user_agent='reddit_sms',
                         username=cred.keyring.get_password('user_login', 'reddit_username'),
                         password=cred.keyring.get_password('user_pass', 'reddit_pass'))

    subreddit1 = reddit.subreddit('Pmsforsale')
    new_subreddit1 = subreddit1.new(limit=100)

    title1 = 'PMSFORSALE: '
    title2 = 'Coins4Sale: '
    currentTime = time.time()
    for submission in new_subreddit1:
        if int(submission.created_utc) > int(currentTime) - 5 * 60: # only run if there are new post in last 5 minutes
            if "WTS" in submission.title:
                title1 += str(submission.title + ' ' + submission.url + '\n\n')

    subreddit2 = reddit.subreddit('Coins4Sale')
    new_subreddit2 = subreddit2.new(limit=100)

    for submission in new_subreddit2:
        if int(submission.created_utc) > int(currentTime) - 5 * 60: # only run if there are new post in last 5 minutes
            if "WTS" in submission.title:
                title2 += str(submission.title + ' ' + submission.url + '\n\n')

    # send text message
    if len(title1) > 0:
        SMS.send(title1)
    if len(title2) > 0:
        SMS.send(title2)

schedule.every(5).minutes.do(myapp)
while True:
    schedule.run_pending()
    time.sleep(1)

