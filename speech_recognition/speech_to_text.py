import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)

    print("Please say something")
    audio = r.listen(source)
    print("Recognizing Now .... ")

    try:
        # recognize speech using google
        converted_text = r.recognize_google(audio)
        print("You have said: \n" + converted_text)
        print("Audio Recorded Successfully \n ")

    except Exception as e:
        print("Error :  " + str(e))

    # write audio
    with open("recorded_audio.wav", "wb") as file:
        file.write(audio.get_wav_data())

    # write text
    with open("recorded_text.txt", "a") as file:
        file.write(converted_text + "\n")
