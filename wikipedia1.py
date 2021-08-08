import wikipedia

userLang = raw_input("1: English\n2: Espanol\n3: Francais\n4: Deutsche\n")
if userLang == "English" or userLang == "english" or userLang == "1":
    outLang = "en"
elif userLang == "Espanol" or userLang == "espanol" or userLang == "2":
    outLang = "es"
elif userLang == "Francais" or userLang == "francais" or userLang == "3":
    outLang = "fr"
elif userLang == "Deutsche" or userLang == "deutsche" or userLang == "4":
    outLang = "de"
else:
    outLang = "en"

while True:
        input = raw_input("Question: ")

        wikipedia.set_lang=(outLang)
        print wikipedia.summary(input, sentences=5)
