from package.pdfpage import PDFPage
from package.pdfinterp import PDFResourceManager
from package.pdfinterp import PDFPageInterpreter
from package.converter import PDFPageAggregator
from package.converter import TextConverter
from package.layout import LAParams, LTTextBox

import os
import logging
import csv
# from pdfminer.pdfparser import PDFParser, PDFDocument
# from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
# from pdfminer.converter import PDFPageAggregator
# from pdfminer.layout import LAParams, LTTextBox, LTTextLine
import io
# alternate method of accessing file
# base_path = "C://some_folder"
# my_file = os.path.join(base_path + "/" + "test_pdf.pdf")
# Loop through base_path

# can make list of pdfs to loop through (read filename, )

password = ""
extracted_text = ""
# print(message_id)
# document requests objects from pdf
# parser stores objects from pdf into document

# parser = PDFParser(fp)
# document = PDFDocument()
# parser.set_document(document)
# document.set_parser(parser)
# document.initialize('')

# Create PDFResourceManager object that stores shared resources such as fonts or images

# rsrcmgr = PDFResourceManager()
resource_manager = PDFResourceManager()
fake_file_handle = io.StringIO()
converter = TextConverter(resource_manager, fake_file_handle, laparams=LAParams())
page_interpreter = PDFPageInterpreter(resource_manager, converter)
# set parameters for analysis

# laparams = LAParams()
# laparams.char_margin = 1.0
# laparams.word_margin = 1.0

# Create a PDFDevice object which translates interpreted information into desired format
# Device needs to be connected to resource manager to store shared resources
# device = PDFDevice(rsrcmgr)
# Extract the decive to page aggregator to get LT object elements
# device = PDFPageAggregator(rsrcmgr, laparams=laparams)

# Create interpreter object to process page content from PDFDocument
# Interpreter needs to be connected to resource manager for shared resources and device
# interpreter = PDFPageInterpreter(rsrcmgr, device)
# for each page in pdf, process text into seperate txt file
with open(f'./aoda.pdf', 'rb') as fh: 
    for index, page in enumerate(PDFPage.get_pages(fh,caching=True, check_extractable=True)):
        # extracted_text = ''
        page_interpreter.process_page(page)
        # The device renders the layout from interpreter
        # extracted_text = split_file.getvalue()
        # print (extracted_text.encode("utf-8"))
        # The outfile should be in binary mode.
        # file_name = f'{file}_{index}.txt'
        # if os.path.isfile(file_name):
        #     expand = 1
        #     while True:
        #         expand += 1
        #         new_file_name = file_name.split(".txt")[0] + str(expand) + ".txt"
        #         if os.path.isfile(new_file_name):
        #             continue
        #         else:
        #             file_name = new_file_name
        #             break
        # # write extracted text to txt file
        # with open(f'{base_path}/Text/{file_name}', "wb") as my_log:
        #     my_log.write(message_id.encode("utf-8"))
        #     my_log.write(extracted_text.encode("utf-8"))
# close the pdf file
        extracted_text = fake_file_handle.getvalue()
# print(extracted_text)
        with open(f'test_{index}.txt', "wb") as my_log:
                my_log.write(extracted_text.encode("utf-8"))
converter.close()
fake_file_handle.close()
print("done")
# ACTUAL BELOW
# listOfPDFs = []
# list_of_msg_id = []
# base_path = "./exchangeemail/Streamline Distributors"
# # base_path = "./exchangeemail/Test"
# directory = os.fsencode(f'{base_path}/temp')
# csvFile = 'log.csv'
# # ---------------------------   Write CSV msg ids to list  --------------------------
# with open(f'{base_path}/tmp_order_items_streamline_distributors.csv', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader: 
#         list_of_msg_id.append(row[0])
# # print(list_of_msg_id)
# # ---------------------------   Attempt at Logging --------------------------
# with open(f'./{csvFile}', "w") as csv_file:
#     # writer = csv.writer(csv_file, delimiter='\t', lineterminator='\n')
#     writer = csv.writer(csv_file, delimiter='\t', lineterminator='\n')
#     # writer.writerow(['Filename' + 'Status'])
#     writer.writerow('Start')

# # ---------------------------   Loop through files in base_path --------------------------
# # ---------------------------   Append their filenames to list   --------------------------
# for file in os.listdir(directory):
#     filename = os.fsdecode(file)
#     if filename.endswith(".pdf"):
#         listOfPDFs.append(filename)

# # ---------------------------   Loop through listOfPDFs list of filenames --------------------------
# # ---------------------------   Process each pdf file into txt      --------------------------
# # for list in listOfFilename
# # fp = open('./testpdf2.pdf', 'rb')
# # for filename in listOfPDFs:
# #   fp = open(filename, 'rb')
# #   password = ""
# #   extracted_text = ""
# # Process each filename in loop

# # ---------------------------   Create log entry for each processed file --------------------------
# # ---------------------------  to trackdown the error invoices      --------------------------
# # log_file = os.path.join(base_path + "/" + "pdf_log.txt")


# # - ----- -- - -DEPRECATED------
# # pull file
# logging.getLogger().setLevel(logging.ERROR)

# for file in listOfPDFs:
#     # fp = open(f'./{base_path}/temp/{file}', 'rb')
#     password = ""
#     extracted_text = ""
#     message_id = ""
#     split_file = file.split(".pdf")[0]
#     for id in list_of_msg_id:
#         # print(id)
#         if split_file in id:
#             message_id = id
#     message_id += "////"
#     # print(message_id)
#     # document requests objects from pdf
#     # parser stores objects from pdf into document

#     # parser = PDFParser(fp)
#     # document = PDFDocument()
#     # parser.set_document(document)
#     # document.set_parser(parser)
#     # document.initialize('')

#     # Create PDFResourceManager object that stores shared resources such as fonts or images

#     # rsrcmgr = PDFResourceManager()
#     resource_manager = PDFResourceManager()
#     fake_file_handle = io.StringIO()
#     converter = TextConverter(resource_manager, fake_file_handle, laparams=LAParams())
#     page_interpreter = PDFPageInterpreter(resource_manager, converter)
#     # set parameters for analysis

#     # laparams = LAParams()
#     # laparams.char_margin = 1.0
#     # laparams.word_margin = 1.0

#     # Create a PDFDevice object which translates interpreted information into desired format
#     # Device needs to be connected to resource manager to store shared resources
#     # device = PDFDevice(rsrcmgr)
#     # Extract the decive to page aggregator to get LT object elements
#     # device = PDFPageAggregator(rsrcmgr, laparams=laparams)

#     # Create interpreter object to process page content from PDFDocument
#     # Interpreter needs to be connected to resource manager for shared resources and device
#     # interpreter = PDFPageInterpreter(rsrcmgr, device)
#     # for each page in pdf, process text into seperate txt file
#     with open(f'./{base_path}/temp/{file}', 'rb') as fh: 
#         for index, page in enumerate(PDFPage.get_pages(fh,caching=True, check_extractable=True)):
#             # extracted_text = ''
#             page_interpreter.process_page(page)
#             # The device renders the layout from interpreter
#             # extracted_text = split_file.getvalue()
#             # print (extracted_text.encode("utf-8"))
#             # The outfile should be in binary mode.
#             # file_name = f'{file}_{index}.txt'
#             # if os.path.isfile(file_name):
#             #     expand = 1
#             #     while True:
#             #         expand += 1
#             #         new_file_name = file_name.split(".txt")[0] + str(expand) + ".txt"
#             #         if os.path.isfile(new_file_name):
#             #             continue
#             #         else:
#             #             file_name = new_file_name
#             #             break
#             # # write extracted text to txt file
#             # with open(f'{base_path}/Text/{file_name}', "wb") as my_log:
#             #     my_log.write(message_id.encode("utf-8"))
#             #     my_log.write(extracted_text.encode("utf-8"))
#     # close the pdf file
#     file_name = f'{file}.txt'
#     extracted_text = fake_file_handle.getvalue()
#     # print(extracted_text)
#     with open(f'{base_path}/Text/{file_name}', "wb") as my_log:
#             my_log.write(message_id.encode("utf-8"))
#             my_log.write(extracted_text.encode("utf-8"))
#     converter.close()
#     fake_file_handle.close()
# print("Task Complete")