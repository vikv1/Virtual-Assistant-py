import speech_recognition


#MICROPHONE FUNCTIONALITY

if input == 'Microphone':
    r = sr.Recognizer()
    with sr.Microphone() as source:
                audio = r.listen(source)
    try:
        self.text.SetValue(r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Sorry, I didn't get that.")
    except sr.RequestError as e:
        print("Sorry, I wasn't able to get the results; {0}".format(e))

#MICROPHONE FUNCTIONALITY
#GOES DIRECTLY BELOW     def OnEnter(self, event):
                        #   input = self.txt.GetValue()
                        #   input = input.lower()
