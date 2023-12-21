import speech_recognition as sr
import pyttsx3 as p
import webbrowser
import wikipedia


def sptx():
    r=sr.Recognizer()
    with sr.Microphone() as Source:
        print("Listening......")
        r.pause_threshold=0.5
        audio=r.listen(Source)
        try:
            print("Recognising....")
            data=r.recognize_google(audio)
            return data
            print("data")
        except:
            print("No voice Recognised")


def txsp(x):
    e=p.init()
    voices=e.getProperty("voices")
    e.setProperty("voice",voices[2].id)
    rate=e.getProperty("rate")
    e.setProperty("rate",140)
    e.say(x)
    e.runAndWait()
txsp("Hello Bhavuk sir,I am your Assistant, How may i help You")

if __name__=="__main__":
    data1=sptx().lower()
    
    if "your name" in data1:
        name="Hello, I am Jarvis, Bhavuk's Voice Assistant"
        txsp(name)
    if "age" in data1:
        age="I am a new born baby"
        txsp(age)
    if "open google" in data1:
        open.webbrowser("https://www.google.com/")
    if "open youtube" in data1:
        open.webbrowser("https://www.youtube.com/")
    if "open instagram" in data1:
        open.webbrowser("https://www.instagram.com/")
    if "open netflix" in data1:
        open.webbrowser("https://www.netflix.com/in/")
    if "open whatsapp" in data1:
        open.webbrowser("https://web.whatsapp.com/")
    if "are u a robot" in data1:
        answer="No I am not a Robot u idiot, I am an AI"
        txsp(answer)
    if "wikipedia" in data1:
        txsp("Searching wikipedia...")
        query=data1.replace("wikipedia","")
        results=wikipedia.summary(query,sentences=1)
        txsp("Accordin to Wikipedia")
        txsp(results)