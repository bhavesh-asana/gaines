from django.shortcuts import render
from django.http import HttpResponse

from PyPDF2 import PdfReader
import pymupdf

def scanner_pymupdf(request):
  doc = pymupdf.open("./textflow/files/ml-handson.pdf")
  content = []
  for page in doc:
    text = page.get_text()
    # print(type(text))
    content.append(text)
  
  return HttpResponse(content)