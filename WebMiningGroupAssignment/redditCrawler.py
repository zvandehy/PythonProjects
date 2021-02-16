import praw

reddit = praw.Reddit(client_id='z0mHSz-y0qOv_A', \
                     client_secret='ggr8fnzoHycbSz9YyJq8ybWG8-A', \
                     user_agent='4010webScraper', \
                     username='testbot4010', \
                     password='4010projectuncc')

subreddit = reddit.subreddit('politics').hot(limit=50)
file = open("redditResults.txt","w") 
total_comments = 0
submission_count = 0
for submission in subreddit:
    file.write("SUBMISSION (" + str(submission_count) + "): " + submission.title + "\n\n")
    submission.comments.replace_more(0)
    comment_count=0
    for topComment in  submission.comments:
        # if comment_count >= 3:
        #     break
        file.write("Comment (" + str(comment_count) + "): " + topComment.body + "\n")
        comment_count+=1
    total_comments +=comment_count
    submission_count +=1
file.write("Total comments: " + str(comment_count))
file.close() 