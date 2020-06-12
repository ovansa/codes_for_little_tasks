import re
import PyPDF2

# 1. Print an f-string that displays NLP stands for Natural Language Processing using the variables provided.

abbr = 'NLP'
full_text = 'Natural Language Processing'

print(f'{abbr} stands for {full_text} \n')

# 2.0 Create a file in the current working directory called contacts.txt by running the cell below

new_file = open('contacts.txt', mode='r')

fields = new_file.read()

print(fields)

new_file.close()

# 3.0 Use PyPDF2 to open the file `Business_Proposal.pdf`. Extract the text of page 2.

open_pdf = open('Business_Proposal.pdf', 'rb')

read_pdf = PyPDF2.PdfFileReader(open_pdf)

page_two_text = read_pdf.getPage(1).extractText()

print(page_two_text)

open_pdf.close()

# 4.0 Open the file contacts.txt in append mode. Add the text of page 2 from above to contacts.txt
#
# open_contact = open('contacts.txt', 'a')
#
# remove_author_pattern = r'[^\wAUTHORS:\]+'
#
# edited_text = ' '.join(re.findall(remove_author_pattern, page_two_text))
#
# open_contact.write(edited_text)
#
# open_contact.close()

# My commented edit above contains a bug
with open('contacts.txt','a+') as c:
    c.write(page_two_text)
    c.seek(0)
    print(c.read())


with open('contacts.txt','a+') as c:
    c.write(page_two_text[8:])
    c.seek(0)
    print(c.read())


email_pattern = r'\w+@\w+.\w{3}'
print(re.findall(email_pattern, page_two_text))
