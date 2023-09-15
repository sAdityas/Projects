import os
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from textblob import TextBlob

YOUTUBE_API_KEY = 'AIzaSyCptYpm9K4A728BOqN6e0cHna0lNu46nws'
yt = build('youtube' , 'v3' , developerKey=YOUTUBE_API_KEY)


def get_Video_Comments(video_id):
    comments = []

    try:
        results = yt.commentThreads().list(
            part = 'snippet',
            videoId = video_id,
            textFormat = 'plainText'
        ).execute()

        while 'items' in results:
            for item in results['items']:
                comment = item['snippet']['topLevelComment']['snippet']["textDisplay"]
                comments.append(comment)

            if 'nextPageToken' in results:
                next_page_token = results['nextPageToken']
                results = yt.commentThreads().list(
                    part='snippet',
                    videoId=video_id,
                    textFormat='plainText',
                    pageToken=next_page_token
                ).execute()
            else:
                break
            
    except HttpError as e:
        print(f"Error Fetching Comments: {e}")
    
    return comments

def analyze_Sentiment(comment):
    analysis = TextBlob(comment)
    sentimentScore = float(analysis.sentiment.polarity)
    if sentimentScore > 0:
        return 1
    elif sentimentScore < 0:
        return -1
    else:
        return 0
    

def rateVideo(video_id):
    comments = get_Video_Comments(video_id)

    if not comments:
        return None
    
    sentimentScores = [float(analyze_Sentiment(comment)) for comment in comments]

    if len(sentimentScores) > 0:
        averageSentiment = sum(sentimentScores) / len(sentimentScores)

    else:
        averageSentiment = 0
    #totalSentiment = sum(analyze_Sentiment(comment) for comment in comments)
    #averageSentiment = totalSentiment / len(comments)

    rating = ((averageSentiment + 1) / 2 ) * 10

    rating = max(1, min(10, rating))

    return rating


def main():
    video_id = 'rVOka3ZqmxQ'
    comments = get_Video_Comments(video_id= 'rVOka3ZqmxQ')
    rating = rateVideo(video_id= 'rVOka3ZqmxQ')

    if comments:
       commentsFile = 'comments.txt'
       with open(commentsFile , 'w' , encoding='UTF-8') as file:
           for comment in comments:
               sentiment = analyze_Sentiment(comment)
               file.flush()
               file.write(f"Comment: {comment}\n")
               file.write(f"Sentiment: {sentiment}\n****************************************************\n\n")
    if comments:
        with open(commentsFile , 'a' , encoding='UTF-8') as file:
            file.write(f"Rating of Video: ")
            if rating is not None:
                file.write(f"{rating:.2f}")
            else:
                return None
            
if __name__ == "__main__":
    main()