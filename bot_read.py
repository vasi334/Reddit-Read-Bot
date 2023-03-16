import praw

with open("credentials.txt", 'r') as f:
    content = f.read()
    lines = content.split('\n')

    client_id = lines[0]
    client_secret = lines[1]
    password = lines[2]
    username = lines[3]
    user_agent = lines[4]
    subreddit_name = lines[5]

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    password=password,
    username=username,
    user_agent=user_agent
)

subreddit = reddit.subreddit(subreddit_name)

try:
    for submission in subreddit.hot(limit=5):
        print("Title: ", submission.title)
        print("Text: ", submission.selftext)
        print("Score: ", submission.score)
        print("---------------------------------\n")
except Exception as e:
    print("An error occurred: ", e)
