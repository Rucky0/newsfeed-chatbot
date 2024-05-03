
import PyPDF2

# Open the PDF files
teslaq1 = open('/Users/bawar/hackathon/newsfeed-chatbot/TSLA-Q1-2023-Update.pdf', 'rb')
teslaq2 = open('/Users/bawar/hackathon/newsfeed-chatbot/TSLA-Q2-2023-Update.pdf', 'rb')
teslaq3 = open('/Users/bawar/hackathon/newsfeed-chatbot/TSLA-Q3-2023-Update-3.pdf', 'rb')
teslaq4 = open('/Users/bawar/hackathon/newsfeed-chatbot/TSLA-Q4-2023-Update.pdf', 'rb')
teslaq5 = open('/Users/bawar/hackathon/newsfeed-chatbot/TSLA-Q1-2024-Update.pdf', 'rb')

# Create PDF reader objects for all the PDF files
pdf_reader_q1 = PyPDF2.PdfReader(teslaq1)
pdf_reader_q2 = PyPDF2.PdfReader(teslaq2)
pdf_reader_q3 = PyPDF2.PdfReader(teslaq3)
pdf_reader_q4 = PyPDF2.PdfReader(teslaq4)
pdf_reader_q5 = PyPDF2.PdfReader(teslaq5)

# Initialize an empty string to store the text
text = ''

# Loop through each page of the PDF files and extract text
for page_num in range(len(pdf_reader_q1.pages)):
    page = pdf_reader_q1.pages[page_num]
    text += page.extract_text()

for page_num in range(len(pdf_reader_q2.pages)):
    page = pdf_reader_q2.pages[page_num]
    text += page.extract_text()

for page_num in range(len(pdf_reader_q3.pages)):
    page = pdf_reader_q3.pages[page_num]
    text += page.extract_text()

for page_num in range(len(pdf_reader_q4.pages)):
    page = pdf_reader_q4.pages[page_num]
    text += page.extract_text()

for page_num in range(len(pdf_reader_q5.pages)):
    page = pdf_reader_q5.pages[page_num]
    text += page.extract_text()

# Close the PDF files
teslaq1.close()
teslaq2.close()
teslaq3.close()
teslaq4.close()
teslaq5.close()

# Write the extracted text to a new text file
output_file = open('/Users/bawar/hackathon/newsfeed-chatbot/tesla_updates.txt', 'w')
output_file.write(text)
output_file.close()

"""
Here's how the code works:

1. First, we import the `PyPDF2` library, which provides functionality for working with PDF files.
2. We open the input PDF file in read-binary mode using `open('input.pdf', 'rb')`.
3. We create a `PdfReader` object from the PDF file using `PyPDF2.PdfReader(pdf_file)`.
4. We initialize an empty string `text` to store the extracted text from the PDF.
5. We loop through each page in the PDF using `range(len(pdf_reader.pages))`.
6. For each page, we get the current page object using `page = pdf_reader.pages[page_num]`.
7. We extract the text from the current page using `page.extract_text()` and append it to the `text` string.
8. After looping through all pages, we close the PDF file using `pdf_file.close()`.
9. Finally, we open a new text file `output.txt` in write mode and write the extracted `text` to the file using `txt_file.write(text)`.

Make sure to replace `'input.pdf'` with the actual path to your input PDF file, and `'output.txt'` with the desired path and filename for the output text file.

Note that you need to install the `PyPDF2` library before running this code. You can install it using pip:

```
pip install PyPDF2
```

Also, keep in mind that this code assumes that the PDF file is not encrypted or password-protected. If the PDF is encrypted, you may need to handle that case separately.
"""