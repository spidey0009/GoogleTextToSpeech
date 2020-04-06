from gtts import gTTS
mytext=input("Enter the speech:")
if len(mytext)==0:
    quit()
else:
        text = gTTS(mytext)
        text.save("text.mp3")
        from playsound import playsound
        playsound("text.mp3")




