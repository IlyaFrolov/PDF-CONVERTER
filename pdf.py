import PyPDF2 as pdf
import copy
import os

print("Введите имя документа: ")
docName = input()
try:
    reader = pdf.PdfFileReader(docName)
except FileNotFoundError:
    print("\nФайл \"{}\" не найден".format(docName))
    exit()

numPages = reader.getNumPages()
newDocWriter = pdf.PdfFileWriter()

for i in range(numPages):
    tempPage1 = reader.getPage(i)
    size = tempPage1.mediaBox.upperRight
    tempPage2 = pdf.pdf.PageObject.createBlankPage(width = size[0], height = size[1])
    tempPage2.mergePage(tempPage1)

    tempPage1.mediaBox.lowerLeft = (0, size[1] / 2)
    tempPage1.mediaBox.lowerRight = (size[0], size[1] / 2)

    tempPage2.mediaBox.upperLeft = (0, size[1] / 2)
    tempPage2.mediaBox.upperRight = (size[0], size[1] / 2)

    tempPage1.rotateCounterClockwise(90)
    tempPage2.rotateCounterClockwise(90)

    newDocWriter.addPage(tempPage1)
    newDocWriter.addPage(tempPage2)

docNameBody, docExt = os.path.splitext(docName)
newDocWriter.write(open(docNameBody + "_edited" + docExt, "bw"))