from PyPDF2 import PdfFileReader

with open('test_pdf.pdf','rb') as infile:

    pdf = PdfFileReader(infile)
    info = pdf.getDocumentInfo()
    n = pdf.getNumPages()

    first_page = pdf.getPage(0)
    text = first_page.extractText()
    print(text)

