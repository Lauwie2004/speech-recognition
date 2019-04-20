import file
import speech_recognition as sr

mic = sr.Microphone(device_index=1)
r = sr.Recognizer()


woord = file.arr()
letters = list(woord)
guessed_word = list(range(int(len(letters))))


for x in range(int(len(letters))):
    guessed_word[x] = "?"

print("The word has %s letters" % len(letters))

def galgje():
    with mic as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)


    guess_good = False
    try:
        input_letter = r.recognize_google(audio)
    except sr.UnknownValueError:
        print("DAFUQ is that!")
        galgje()

    print(input_letter)

    for i in range(int(len(letters))):
        for n in letters:
                if letters[i] == input_letter[0]:
                    guessed_word[i] = input_letter[0]
                    guess_good = True

    if guess_good != False:
        print("Guessed letter was correct, go on!")
    else:
        print("incorrect")


    print_woord = ""

    for x in guessed_word:
        print_woord += x

    if guessed_word == letters:
        print("Good, the word was %s" % woord)
    else:
        print("You now have %s" % print_woord)
        galgje()


galgje()
input("Press enter to exit")
