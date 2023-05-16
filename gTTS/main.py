import gtts
from playsound import playsound


tts = gtts.gTTS("Hello Matilda. I like cats. Even though I am a robot dog.")

tts.save("hello.mp3")

playsound("hello.mp3")