# Hunter Thornsberry
# Get the most recent post to a subreddit and emails them to you if they match a criteria
# hunter@hunterthornsberry.com

import praw
import urllib3
import sendemail
import time
from prawcore.exceptions import PrawcoreException
import logging

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
logger = logging.getLogger('prawcore')
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

urllib3.disable_warnings()

reddit = praw.Reddit(client_id='ID',
                     client_secret='SECRET',
                     password='PASSWORD',
                     user_agent='USER_AGENT',
                     username='USERNAME')


# Criteria (string to search in Submission Title)
criteria = ""

# Subreddit to search (Ex: /r/pics would be "pics")
subreddit = ""

# Email to send results to
email = ""

# Subject of results email
subject = ""

# Stream Submissions
def run():
    # If the bot does timeout then we don't want to get the same emails
    # We accomplish this by checking that the submissions are new as of run time
    # Reddit submissions are ~3 hours from Eastern Time where I live, adjust as needed
    startTime = float(time.time()) + 28800
    while True:
        try:
            for submission in reddit.subreddit(subreddit).stream.submissions():
                if submission.created > startTime: # Check the time
                    if criteria in str(submission.title).lower():
                        print submission.title
                        print submission.url
                        print submission.shortlink
                        sendemail.send_email(email, subject, submission.title.split(" ", 1)[1] + "\n" + submission.url + "\n" + submission.shortlink)
        except PrawcoreException:
            # Timeouts happen a lot, to keep the bot running wait 60 seconds and then start again
            time.sleep(60)
            run()

# Run the code
run()
