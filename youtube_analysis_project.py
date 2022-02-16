# -*- coding: utf-8 -*-
"""youtube analysis project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RVE3NbANYIhd1VaWJk0lj3QyfX49LK93
"""

#import libraries
from googleapiclient.discovery import build
import pandas as pd

# api key that I choose
api_key = #insert api key
# Videos ids
video_ids = ['lEljKc9ZtU8',
            'YcqVWFZXyaE',
            'kLUuegj9D9E',
            'OMUEmWGxoVg',
            'qkxuFKqJXWY',
            'iLcvvVXBSFo',
            'KdgQvgE3ji4',
            'xC-c7E5PK0Y',
            'WSbgixdC9g8',
            'VwVg9jCtqaU'
            ]

youtube = build('youtube','v3',developerKey=api_key)

# UDF to fetch videos details using Youtube API
def get_video_stats(youtube,video_ids):
  all_data = []
  request = youtube.videos().list(
               part="snippet,contentDetails,statistics",
               id=','.join(video_ids))
  response = request.execute()

  for i in range(len(response['items'])):
    data = dict(Video_Id = response['items'][i]['id'],
                Title = response['items'][i]['snippet']['title'],
                Date_of_Publish = response['items'][i]['snippet']['publishedAt'],
                view = response['items'][i]['statistics']['viewCount'],
                Likes = response['items'][i]['statistics']['likeCount'],
                Dislikes = response['items'][i]['statistics']['favoriteCount'])  #cant find dislike section in file so assign (Dislike=favoritecount)
    all_data.append(data)
              
  return all_data

#contain udf in variable
video_statistics = get_video_stats(youtube,video_ids)

#loading varible in dataframe
video_data = pd.DataFrame(video_statistics)

video_data

#dump output into a CSV file
video_data.to_csv('video_data.csv')

cat video_data.csv
