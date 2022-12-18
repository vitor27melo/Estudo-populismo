import PyPDF2
import glob


path = 'C:/Users/Vitor/Documents/Faculdade/FLP0472 - Governo Representativo/Artigo/Arquivos/PDF/Lula/*/*.pdf'
pdfs = glob.glob(path)
counter = 0
for pdf in pdfs:
    pdfFileObj = open(pdf, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    text = ""
    for i in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(i)
        text = text + pageObj.extractText()
    pdfFileObj.close()
    file = open(pdf + ".txt", "w")
    text = text.replace('\uf0a7', '')
    text = text.replace('\u201f', '')
    file.write(text)
    file.close()


