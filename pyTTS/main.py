import pyttsx3

engine = pyttsx3.init()

text = "Hello Derek"
engine.say(text)
# play the speech
engine.runAndWait()

# get details of speaking rate
rate = engine.getProperty("rate")
print(rate)

# get details of all voices available
voices = engine.getProperty("voices")
print(voices)

engine.save_to_file(text, "python.mp3")
engine.runAndWait()

