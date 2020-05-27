import  PyPDF2
import sys
# with open('data/dummy.pdf', 'rb') as file:
#     reader = PyPDF2.PdfFileReader(file)
#     page = reader.getPage((0))
#     page.rotateClockwise(90)
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page)
#     with open('tilt.pdf', 'wb') as newfile:
#         writer.write(newfile)


#grap all given files into list except the first one whic is pythpn itself
# input = sys.argv[1:]
# def pdf_combiner(pdf_list):
#     merger = PyPDF2.PdfFileMerger()
#     for pdf in pdf_list:
#         merger.append(pdf)
#     merger.write('data/super.pdf')
#
# pdf_combiner(input)

def create_watermark(input, output,watermark):

    #get the watermark
    water_read = PyPDF2.PdfFileReader(watermark)
    water_page = water_read.getPage(0)

    #read the pdf file
    input_read = PyPDF2.PdfFileReader(input)

    pdf_writer = PyPDF2.PdfFileWriter()

    for page in range(input_read.getNumPages()):
        page = input_read.getPage(page)
        page.mergePage(water_page)
        pdf_writer.addPage(page)

    with open(output, 'wb') as out:
        pdf_writer.write(out)

create_watermark(
    input='data/super.pdf',
    output='data/new_file_with_water.pdf',
    watermark='data/water.pdf'
)


