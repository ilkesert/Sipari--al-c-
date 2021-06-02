import cv2
import time
from gtts import gTTS
import speech_recognition as sr
from playsound import playsound
import os
import random


def speak(string):
    tts = gTTS(string, lang='tr')
    rand = random.randint(1, 10000)
    file = 'audio-' + str(rand) + '.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)

def Komutal():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Dinliyorum")
        speak("Dinliyorum")
        audio = r.listen(source)

        try:
            durum = r.recognize_google(audio, language='tr-tr')
            print(f"user said:{durum}\n")

        except Exception as e:
            speak("Rica etsem tekrar söyler misiniz?")
            return "None"
        return durum

face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
face_cascade.load(r'A:\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml')
webcam = cv2.VideoCapture(0)
cv2.destroyAllWindows()
while True:
    succsessfull_frame_read, frame = webcam.read()
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_coordinates = face_cascade.detectMultiScale(grayscaled_img)
    i = 0
    for (x, y, w, h) in face_coordinates:
        i = i + 1
        if i < 3:
            time.sleep(0)
        elif i >= 3:
            speak("Hoşgeldiniz efendim. Başlangıç olarak hangi çorbayı seçersiniz")
            print("Mercimek Çorbası, Ezogelin Çorbası, Balık Çorbası, Yayla Çorbası, Tavuk Çorbası")
            corba = Komutal()
            speak("Madem" + corba+ "nı seçtiniz peki ana yemek olarak ne istersiniz?")
            print("Biftek, Hamburger, Pizza, Ekşili köfte, İçli köfte, Izgara köfte")
            anayemek = Komutal()
            speak(anayemek +"Güzel seçim. Peki tatlı olarak ne istersiniz?")
            print("Kazandibi, Tavukgöğüsü, Puding, Baklava, Güllaç")
            tatli = Komutal()
            speak("Son olarak İçecek olarak ne istersiniz?")
            icecek = Komutal()
            speak("Siparişiniz geliyor efendim Afiyet olsun.")

            print(corba)
            print(anayemek)
            print(tatli)
            print(icecek)
