import pyttsx3
import datetime
import speech_recognition as sr
import setuptools 
import wikipedia
import webbrowser
import smtplib
import os



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning sir")
    elif hour>12 and hour<18:
        speak("Good afternoon sir")
    else: speak("Good evening sir")  
    speak("I'm Jarvis here your AI assistant")  

def takecommand():
    #mic-access
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ..")
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio,language='en-in')   
        print(f"user said:{query}\n")
    except Exception as e:
       print(e) 
       print("say it again please...")
       return "None"
    return query

def sendemail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('daddybhai29@gmail.com','daddy@29')
    server.sendmail('daddybhai29@gmail.com',to,content)
    server.close


if __name__=="__main__":
    speak("welcome !")    
    wishme()   
    while True:
      query = takecommand().lower() 

      if 'wikipedia' in query:
          speak('searching wikipedia..')
          query=query.replace("wikipedia","")
          results = wikipedia.summary(query,sentences=2)
          print(results)
          speak('according to wikipedia')
          speak(results)
         
      elif 'open youtube' in query:
          speak('opening youtube sir..')
          webbrowser.open('youtube.com')
          
      elif 'portfolio' in query:
          #codepath = "C:\\Users\\Public\\Libraries\\Microsoft VS Code\\Code.exe"  
          #os.startfile(codepath)
          portfolio = "C:\\MinGW\\mingw32\\bin\\web devlopment\\portfolio.html"
          os.startfile(portfolio)  

      elif 'send mail' in query:
          speak('opening mail sir..')
          try:
              speak('what should i say ?')
              content = takecommand() 
              to = "daddybhai29@gmail.com"
              sendemail(to,content)
              speak('mail sent successfully sir.')
          except Exception as e:
              print(e)
              speak('sorry sir cant send mail')

      elif 'blue eyes' in query:
          speak('playing blue eyes by yoyo honey singh..')
          webbrowser.open('https://www.youtube.com/watch?v=NbyHNASFi6U')  

      elif 'open my insta' in query:
          speak('opening instagram ..')
          webbrowser.open('https://www.instagram.com/?next=%2F')
      elif 'open chat GPT' in query:
          speak('opening chatgpt ..')
          webbrowser.open('https://chatgpt.com')    
      elif 'food' in query:
        speak('sure sir ..from which site ?')
      elif 'swiggy' in query:
              speak('swiggy has crazy discounts these days ..opening swiggy sir ..')
              webbrowser.open('https://www.swiggy.com/') 
      elif'zomato' in query:
              speak('better alternative of swiggy is zomato .. opening zomato sir')
              webbrowser.open('https://www.zomato.com/ncr/golf-course-order-online')
              

      elif 'mc stan' in query:
          speak('cha pri') 
      elif 'hello' in query:
          speak('hi there. How are you ?') 
      elif 'how are you' in query:
          speak('i am fine. How about you ?' )  
      elif 'my laptop' in query:
          speak('laptop name : Samsung book 2 pro. powered by 12th Gen intel core i5 P processor. Key highlight is weight which is 850 grams.')    
      elif 'add numbers' in query:
          speak('Sure sir. write the numbers please' )
          a = int(input("a="))
          b = int(input("b="))
          print((a+b))
          speak('ans is', (a+b))
          
      elif'exit' in query:
           speak("Goodbye sir, have a great day!")
           break
  