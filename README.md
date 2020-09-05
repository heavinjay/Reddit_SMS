# Reddit_SMS
This application is used to send automated text messages when a post is made that includes keywords. The text message will include the title of the post
along with a clickable URL to take you directly to the post. The intention of this application is so that you may be notified as soon as possible when a
post is made that could interest you. This application is currently set to check every 5 minutes for [WTS] tags in post titles within two subreddits. If
a new post is found it will automatically send off the text message to notify you. The text message is configured to route through your email providers 
server, thus requiring you to enter your email login information. To run this application you should first navigate to the cred.py file and update it with your
credentials. Afterwards update the user agent in the app.py file. After completing this the app will be able to run.
