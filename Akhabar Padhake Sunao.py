import time
import json 
import requests
from  win32com.client import Dispatch


def speak(str):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__=='__main__':
    #speak(str)
    url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=5a69b728f11b4fba9bf91a58fc91a92f'
    news = requests.get(url).text
    news = json.loads(news)
    arts = news['articles']
    speak('''Top Headline news for today are ''')
    for article in arts:
        print(article['title'])
        speak(article['title'])
        
        speak('Next News..')
