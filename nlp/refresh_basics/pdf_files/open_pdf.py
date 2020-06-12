import PyPDF2


#1. Open and read a pdf file
myfile = open('Immunology.pdf', mode='rb')
pdf_reader = PyPDF2.PdfFileReader(myfile)

# 1.0 Print no of pages in pdf PdfFileReader
# print(f'{pdf_reader.numPages} Pages')

#1.1 Get a single page and extract text

#1.2 Add a new page to a pdf
f = open('Immunology.pdf', mode='rb')

# Get the first page
pdf_reader = PyPDF2.PdfFileReader(f)
first_page = pdf_reader.getPage(0)

pdf_writer = PyPDF2.PdfFileWriter()
pdf_writer.addPage(first_page)

pdf_output = open('new_pdf.pdf', 'wb')
pdf_writer.write(pdf_output)
pdf_output.close()
f.close()

# Read new file

brand_new = open('new_pdf.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(brand_new)
print(f'{pdf_reader.numPages} Pages\n\n')


f = open('new_pdf.pdf', mode='rb')
pdf_text = []
pdf_reader = PyPDF2.PdfFileReader(f)
for p in range(pdf_reader.numPages):
    page = pdf_reader.getPage(p)
    pdf_text.append(page.extractText())

print(f'{len(pdf_text)} Pages\n\n')
# print(pdf_text)
f.close()

for page in pdf_text:
    print(f'{page} \n')
