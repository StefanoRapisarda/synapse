import qpageview
import sys

from PyQt5.Qt import *
a = QApplication(sys.argv)

pdf_file = '/Users/xizg0003/Downloads/AppBreweryCornellNotesTemplateSinglePage.pdf'
v = qpageview.View()
v.show()
doc = qpageview.loadPdf(pdf_file)
v.setDocument(doc)

sys.exit(a.exec_())
