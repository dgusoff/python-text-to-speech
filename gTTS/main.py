import gtts
from playsound import playsound
from pydub import AudioSegment


tts = gtts.gTTS("Hello.")

tts.save("hello.mp3")

sound = AudioSegment.from_mp3("hello.mp3")
sound.export("hello.wav", format="wav")



playsound("hello.mp3")