import speech_recognition as sr
import json
#import pyttsx
#engine = pyttsx.init()
from os import system
from gtts import gTTS
import os


#os.system("mpg321 error.mp3")

# obtain audio from the microphone

# keywords = [("alpha", 0.5), ("bravo", 0.5), ("charlie", 0.5), ("delta", 0.5), ("echo", 0.5), ("foxtrot", 0.5), ("golf", 0.5), ("hotel", 0.5)]

# # recognize speech using Sphinx
# try:
#     print("Sphinx thinks you said " + r.recognize_sphinx(audio))
# except sr.UnknownValueError:
#     print("Sphinx could not understand audio")
# except sr.RequestError as e:
#     print("Sphinx error; {0}".format(e))

# # recognize speech using Google Speech Recognition
# try:
#     # for testing purposes, we're just using the default API key
#     # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
#     # instead of `r.recognize_google(audio)`
#     # print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
#     results = r.recognize_google(audio, show_all = True)
#     print(results)
# except sr.UnknownValueError:
#     print("Google Speech Recognition could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from Google Speech Recognition service; {0}".format(e))

def read_file(path):
    file = open(path, "r")
    data = file.read()
    file.close()
    return data

def read_json(path):
    return json.loads(read_file(path))


def voice_input(audio, r):
    # recognize speech using Google Cloud Speech
    GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"vernal-byway-233402-ebd72f47d369.json"
    try:
        speech = (r.recognize_google_cloud(audio, preferred_phrases = ["alpha", "bravo", "charlie", "delta", "echo", "foxtrot", "golf", "hotel", "one", "two", "three", "four", "five", "six", "seven", "eight", "move"], credentials_json=json.dumps(read_json(GOOGLE_CLOUD_SPEECH_CREDENTIALS))))
        #speech = (r.recognize_google_cloud(audio, credentials_json=json.dumps(read_json(GOOGLE_CLOUD_SPEECH_CREDENTIALS))))
        print(speech)
        return speech
        #print("Google Cloud Speech thinks you said " + r.recognize_google_cloud(audio, credentials_json=json.dumps(read_json(GOOGLE_CLOUD_SPEECH_CREDENTIALS))))
    except sr.UnknownValueError:
        print("Google Cloud Speech could not understand audio")
        return None
    except sr.RequestError as e:
        print("Could not request results from Google Cloud Speech service; {0}".format(e))
        return None
    return None

def common_letters(word, arr):
    counter = 0
    maxmatch = 0
    match=None
    word = word.lower()
    if word in arr:
        return arr[word]
    if word in arr.values():
        return word
    for possibility in arr.keys():
        #print(counter)
        for i in word:
            if i in possibility:
                counter = counter + 1
        if word[0] == possibility[0]:
            counter = counter+5
        if counter > maxmatch:
            match = possibility
            maxmatch = counter
        #print("possibility", possibility, " count is ", counter)
        #print(possibility[0])
        counter = 0
    return arr[match]




def parse_speech(speech):
    if not speech:
        return None
    words = speech.split()
    if len(words) > 5:
        return None
    command = []
    try:
        for index in range(0,len(words)):
            print(words[index])
            if words[index] in ['move', 'movie'] or words[index][0].lower() == 'm':
                command.append("to")
            else:
                if index == 0 or index == 3:
                    word = common_letters(words[index], alphabet)
                else:
                    word = common_letters(words[index], numbers)
                command.append(word)
                print(word)
    except:
        return None

    return command


def get_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)  # we only need to calibrate once, before we start listening
        os.system("next.mp3")
        print("Talk now")
        audio = r.listen(source)
        #audio = r.listen(source, snowboy_configuration = snowboy)'
    print("Processing")
    speech = voice_input(audio, r)
    #speech = "Alpha One move hotel to"
    command = parse_speech(speech)
    #print(command)
    if command:
        tts = gTTS(text=(" ".join(command)), lang='en')
        tts.save("move.mp3")
        os.system("move.mp3")
        #system('say '+command)
        #engine.say(command)
        #engine.runAndWait()
    else:
        os.system("error.mp3")
        return None
        #engine.say("Sorry, I didn't get that. Please try again")
        #engine.runAndWait()

    # for i in range(0, len(command)):
    #     if command[i] in alphanumeric:
    #         command[i] = alphanumeric[command[i]]
    command = command[ :2] + command[3: ]
    print(command)
    ret_str = ""
    for element in command:
        ret_str+=element
    return ret_str


snowboy = ("/Users/jlchew/Downloads/osx-x86_64-1.1.1", ["/Users/jlchew/Downloads/osx-x86_64-1.1.1/chess.pmdl"])

legal_words = ["alpha", "bravo", "charlie", "delta", "echo", "foxtrot", "golf", "hotel", "one", "two", "three", "four", "five", "six", "seven", "eight"]

alphabet = {"alpha": 'A', "bravo": 'B', "charlie": 'C', "delta":'D', "echo":'E', "foxtrot": 'F', "golf": 'G', "hotel": 'H'}

numbers = {"one": '1', "two": '2', "three": '3', "four": '4', "five": '5', "six": '6', "seven":'7', "eight":'8'}

alphanumeric = {"A": '1', "B": '2', "C": '3', "D": '4', "E": '5', "F": '6', "G":'7', "H":'8'}

tts = gTTS(text='Sorry, I did not understand that. Can you try again?', lang='en')
tts.save("error.mp3")
tts = gTTS(text='Next move please', lang='en')
tts.save("next.mp3")

#print(get_command())
