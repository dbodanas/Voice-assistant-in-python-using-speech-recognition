from datetime import datetime
import speech_recognition as sr
import pyttsx3
import wikipedia
import os
import webbrowser
from newsapi import NewsApiClient
import requests
from  pprint import pprint

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0 ].id)
chromepath='C:/Program Files/Google/Chrome/Application/chrome.exe %s'

def speak(audio):
  engine.say(audio)
  engine.runAndWait()
#function to wish the user.
def wishme():
  hour=int(datetime.now().hour)
  if hour>=0 and hour<12:
    speak("Good Morning!")

  elif hour>=12 and hour<16:
    speak("Good Afternoon!")

  elif hour>=16 and hour<19:
    speak("Good Evening!")

  else:
    speak("hello!")

  speak("I am the Device's AI, How may I help You")

def takecommand():
  recognizer=sr.Recognizer()
  with sr.Microphone() as mic:
    print("listening....")
    recognizer.pause_threshold=1 
    recognizer.energy_threshold=6000
    audio=recognizer.listen(mic)

  try:
    print("recognizing...")
    query=recognizer.recognize_google(audio, language='en-in')
    print(f"you said: {query}\n")
  
  except Exception as e:
    print(e)
    speak("say that again")
    return "None"
  
  return query
    


if __name__=="__main__":
  wishme()
  while True:
    query=takecommand().lower()
    if 'wikipedia' in query:
      speak('searching wikipedia')
      query=query.replace('wikipedia','')
      results= wikipedia.summary(query)
      speak("according to wikipedia")
      print(results)
      speak(results)
      
# function to open Youtube.

    elif 'open youtube' in query:
      webbrowser.get(chromepath).open('youtube.com')

# function to Play music.

    elif 'play music' in query:
      dir='C:\\Users\\Lenovo\\Music\\Playlists'
      songs = os.listdir(dir)
      print(songs)
      os.startfile(os.path.join(dir,songs[0]))

# function to tell time.

    elif 'time' in query:
      strTime=datetime.now().strftime("%H:%M:%S")
      print(f"current time is {strTime}")
      speak(f"current time is {strTime}")

# function to open vs code.

    elif 'open vs code' in query:
      path="C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
      os.startfile(path)

# function to open Chrome.

    elif 'open chrome' in query:
      chromepath="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
      os.startfile(chromepath)

# function to search in Chrome.

    elif 'in chrome' in query:
      try:
        speak('searching...')
        query=query.replace('in chrome','')
        print("you're searching for "+query)
        url='https://www.google.com/search?gs_ssp=eJzj4tLP1TfIyIs3N0ozYPTizcxLyUzMS1TIys9LLQYAcP4Irw&q='
        search=url+query
        webbrowser.get(chromepath).open(search)
        
      except Exception as e:
        print(e)
        speak('unable to process the search, please try again')

# function for telling news.    

    elif 'in news' in query:
      newsapi = NewsApiClient(api_key='4639226a2fe4498f97f9c0c7c37bc565')
      query=query.replace('in news','')
      news_sources = newsapi.get_sources()
      for source in news_sources['sources']:
        pass
        #print(source['name'])
      top_headlines = newsapi.get_top_headlines(q=query,language='en')
      for article in top_headlines['articles']:
        print('Title : ',article['title'])
        speak(article['title'])
        print('Description : ',article['description'],'\n\n')
        speak(article['description'])

# function for telling weather.     

    elif 'weather in' in query:
      query=query.replace('weather in','')
      API_key='cfce5763f9b5bcf9d747d9af568ccb6e'
      weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={query}&appid="
      final_url = weather_url + API_key
      weather_data = requests.get(final_url).json()
      pprint(weather_data)
      speak(weather_data)