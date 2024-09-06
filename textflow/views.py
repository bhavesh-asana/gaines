from django.http import HttpResponse

import pymupdf

import os
import glob

# Define the directory path where your files are stored
directory_path = './textflow/files/'

# Use glob to find all files in the directory (e.g., *.pdf for all PDF files)
file_paths = glob.glob(os.path.join(directory_path, '*.pdf'))

# Scanning all the files in a directory
def scan_folder(request):
  content = []
  # Loop through each file and read its contents
  for file_path in file_paths:
    with pymupdf.open(file_path) as doc:
      for page in doc:
        text = page.get_text()
        content.append(text)
    print("Finished Reading : " + file_path)
  return HttpResponse(content)

# Scanning an individual file
def scanner_pymupdf(request):
  doc = pymupdf.open("./textflow/files/ml-handson.pdf")
  content = []
  for page in doc:
    text = page.get_text()
    # print(type(text))
    content.append(text)
  return HttpResponse(content)
