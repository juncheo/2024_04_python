from gtts import gTTS

text = "수업 끝나면 운동하러가야해 알베긴다"

a = gTTS(text,lang='ko')
a.save('result.mp3')