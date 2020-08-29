import pyttsx3\
import pypdf2
from tkinter.filedialog import *
book = askopenfilename(Linux_commnd with example)
pdfreader = pypdf2.pdfFileReader(book)
pages = pdfreader.numpages
for number in range(1,pages):
page = pdfreader.getPage(number)
text = page.extractText()
player = pyttsx3.init()
player.say(text)
player.runAndWait()