import PyPDF2
def pdf_read(path):
    pdf_content = ""
    with open(path.name, 'rb') as file:
        # Create a PDF reader object
        reader = PyPDF2.PdfReader(file)

        # Get the number of pages in the PDF file
        num_pages = len(reader.pages)

        # Loop over each page in the PDF file
        for page in range(num_pages):
            # Get the text content of the page
            text = reader.pages[page].extract_text()
            pdf_content += text + " "

        return pdf_content

