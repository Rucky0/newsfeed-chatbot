from pdf2image import convert_from_path

# Path to your PDF file
pdf_path = 'TSLA-Q1-2023-Update.pdf'

# Convert PDF to images
images = convert_from_path(pdf_path)

# Save each page as an image
for i, image in enumerate(images):
    image.save(f'{pdf_path}_page_{i}.jpg', 'JPEG')
