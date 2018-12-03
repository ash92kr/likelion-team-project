from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
import json
import pandas as pd
import numpy as np


class BookIndex(TemplateView):
    template_name = 'book/book_index.html'

def book_python(request):
    word = request.GET.get('search')
    
    with open('./book/{}.json'.format(word)) as f:
        key = f.read().encode('utf-8')
        data = json.loads(key)
        
    center = pd.read_csv('./book/center.csv')
        
    
    df = pd.DataFrame(list(data.values()), index = data.keys())
    
    # print(df)
    # print(center)
    li = []
    for i in range(8):
        
        ccc = np.array(center.iloc[i,1:])
        print('cccccccccc' , ccc)
        sim = df.iloc[:,:-2].dot(ccc)
        
        # print('col =======> ' , df.iloc[:,:-2])
        # df.loc[]
    
        li.append(sim.nlargest(5))
    # print(sim.nlargest(10))
    print('col =======> ' , df.iloc[:,:-2])
    
    # print(type(sim))
    
    # print(li[0])
    books = {}
    for book_q in li[0].index:
        books[book_q] = df['link'][book_q]
        # print(df['link'][book])
    # sim = list(li[0]).split()

    books1 = {}
    for book_w in li[1].index:
        books1[book_w] = df['link'][book_w]
        # print(df['link'][book])
    # sim = list(li[0]).split()

    books2 = {}
    for book_e in li[3].index:
        books2[book_e] = df['link'][book_e]
        # print(df['link'][book])
    # sim = list(li[0]).split()

    books3 = {}
    for book_r in li[6].index:
        books3[book_r] = df['link'][book_r]
        # print(df['link'][book])
    # sim = list(li[0]).split()

 
    
    return render(request, 'book/book_index.html', {'books' : books, 'books1': books1, 'books2' : books2, 'books3' : books3})