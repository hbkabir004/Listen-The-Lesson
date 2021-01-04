import pyttsx3
import PyPDF2
book = open('OS_Book.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
keka = pyttsx3.init()
keka.say('Welcome to our project "Smart Audio Book" done by Abir and Keka')

abir = pyttsx3.init()
for num in range(24, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    abir.say(text)
    abir.runAndWait()