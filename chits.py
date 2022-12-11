from PyPDF2 import PdfFileReader, PdfFileWriter
def chit_fun(filename):
    pdf_document = filename.replace(" ","_")
    pdf = PdfFileReader("static/files/"+pdf_document)

    en = int(pdf.getNumPages()/2)
    en = 0 if en%3==0 else  ((int(en/3)+1)*3)-en

    output_filename_even = "Back.pdf"
    output_filename_odd = "Front.pdf"

    pdf_writer_even = PdfFileWriter()
    pdf_writer_odd = PdfFileWriter()
    pdf_swap_even = PdfFileWriter()
    for page in range(pdf.getNumPages()):
        current_page = pdf.getPage(page)
        if page % 2 == 0:
            pdf_writer_odd.addPage(current_page)
        else:
            pdf_writer_even.addPage(current_page)

    with open("static/files/"+output_filename_odd, "wb") as out:
         pdf_writer_odd.write(out)

    for i in range(en):
        pdf_writer_even.add_blank_page()

    for i in range(0,pdf_writer_even.getNumPages(),3):    
        pdf_swap_even.addPage(pdf_writer_even.getPage(i+2))
        pdf_swap_even.addPage(pdf_writer_even.getPage(i+1))
        pdf_swap_even.addPage(pdf_writer_even.getPage(i))
 
    with open("static/files/"+output_filename_even, "wb") as out:
        pdf_swap_even.write(out)
        