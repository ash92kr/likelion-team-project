from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
import json
import pandas as pd


class BookIndex(TemplateView):
    template_name = 'book/book_index.html'

def book_python(request):
    word = request.GET.get('search')
    book_df = json.load('/book/python.json')#.format(word))

    print(book_df)
    return render(request, 'book/book_index.html')