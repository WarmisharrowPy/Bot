import pyttsx3
import speech_recognition as bot
from pywikihow import search_wikihow

listener = bot.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
  engine.say(text)
  engine.runAndWait()



def take_command():
    try:
      with bot.Microphone() as source:
        print('listening...')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'bot' in command:
                    print(command)

    except:
        pass
    return command


def run_bot():
    command = take_command()
    if 'how to' in command:
        talk('please tell what do you want to do?')
        want = take_command()
        want = want.replace('jarvis', '')
        max_result = 1
        how_to_func = search_wikihow(want, max_result)
        assert len(how_to_func) == 1
        how_to_func[0].print()
        talk(how_to_func[0].summary)

while True:
    run_bot()