import os
import PyPDF2

from tkinter import Tk
from tkinter.filedialog import askopenfile

Tk().withdraw()
filelocation=askopenfile
with open(filelocation, "rb") as f:
    pdf=PyPDF2.PdfFileReader(f)
    myText=""
    for pageNum in range(pdf.numPages):
        pageobj=pdf.getPage(pageNum)
        myText += pageobj.extract_text()
print(myText)

final_output= gTTS(text=myText,lang="en")    
print("Generating Speech.....")  
final_output.save("Generated_Speech.mp3")  
os.system("Start_Generated_Speech.mp3")
print("successfully generated")
