from PyPDF2 import PdfWriter
import os
merge = PdfWriter()
files =[file for file in os.listdir() if file.endswith(".pdf")]

for pdf in ["File1.pdf", "filr2.pdf", "File3.pdf"]:
    merge.append(pdf)
merge.write("merge-pdf.pdf")
merge.close() 