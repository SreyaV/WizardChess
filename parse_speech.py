import speech_recognition as sr
import json

snowboy_configuration = ("/Users/jlchew/Downloads/osx-x86_64-1.1.1", ["/Users/jlchew/Downloads/osx-x86_64-1.1.1/chess.pmdl"])
<<<<<<< HEAD

global legal_words = ["alpha", "bravo", "charlie", "delta", "echo", "foxtrot", "golf", "hotel", "one", "two", "three", "four", "five", "six", "seven", "eight", "move"]
global alphabet = {"alpha": 'A', "bravo": 'B', "charlie": 'C', "delta":'D', "echo":'E', "foxtrot": 'F', "golf": 'G', "hotel": 'H'}
global numbers = {"one": '1', "two": '2', "three": '3', "four": '4', "five": '5', "six": '6', "seven":'7', "eight:'8'"}
=======
>>>>>>> 309b78936db40e20b12a2dec1c7dc961eb8b8f4c
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


def voice_input():
    # recognize speech using Google Cloud Speech
    GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"/Users/jlchew/Downloads/MakeMIT 2019-acab376edd58.json"
    try:
        speech = (r.recognize_google_cloud(audio, preferred_phrases = ["alpha", "bravo", "charlie", "delta", "echo", "foxtrot", "golf", "hotel", "one", "two", "three", "four", "five", "six", "seven", "eight", "move"], credentials_json=json.dumps(read_json(GOOGLE_CLOUD_SPEECH_CREDENTIALS))))
        #speech = (r.recognize_google_cloud(audio, credentials_json=json.dumps(read_json(GOOGLE_CLOUD_SPEECH_CREDENTIALS)))
        return speech
        #print("Google Cloud Speech thinks you said " + r.recognize_google_cloud(audio, credentials_json=json.dumps(read_json(GOOGLE_CLOUD_SPEECH_CREDENTIALS))))
    except sr.UnknownValueError:
        print("Google Cloud Speech could not understand audio")
        return None
    except sr.RequestError as e:
        print("Could not request results from Google Cloud Speech service; {0}".format(e))
        return None
    return None


def parse_speech(speech):
<<<<<<< HEAD
    if not speech:
        return False
    words = speech.split()
    command = []
    for word in words:
        if word in legal_words:
            command.append(word)
        else:



=======
    if speech:
        print(speech)
    return None

>>>>>>> 309b78936db40e20b12a2dec1c7dc961eb8b8f4c
r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)  # we only need to calibrate once, before we start listening
    print("Say something!")
    audio = r.listen(source)
speech = voice_input()
parse_speech(speech)
