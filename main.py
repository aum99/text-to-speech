from gtts import gTTS
from tkinter import filedialog
from tkinter import Tk
import PyPDF2

root = Tk()
root.withdraw()
filename = filedialog.askopenfilename(initialdir='/Users/aumravibattul/Downloads', title='Select the text file: ')


def convert_to_audiobook(textfile):
    with open (textfile, 'r+b') as tf:
        pdf_reader = PyPDF2.PdfFileReader(tf)
        pages = pdf_reader.numPages
        for page in range(pages):
            pageObj = pdf_reader.getPage(page)
            words = [i.replace("\n", "") for i in pageObj.extractText().split(" ")]
            text=''
            for i in words:
                text += f" {i}"
        print(text)
        tts = gTTS(text, lang='en')
        tts.save('audiobook.mp3')
    tf.close()


convert_to_audiobook(filename)
