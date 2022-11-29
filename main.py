from gtts import gTTS
from tkinter import filedialog
from tkinter import Tk

root = Tk()
root.withdraw()
filename = filedialog.askopenfilename(initialdir='/Users/aumravibattul/Downloads', title='Select the text file: ')


def convert_to_audiobook(textfile):
    with open (filename) as tf:
        lines = tf.readlines()
        text = ''
        for line in lines:
            text += line
        print(lines)
        tts = gTTS(text, lang='en')
        tts.save('audiobook.mp3')
    tf.close()


convert_to_audiobook(filename)
