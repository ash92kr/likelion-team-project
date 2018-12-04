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
    cluster_li = {'SQL' : [0,1,2,3], '리눅스' : [0,1,2,3], '자바' : [1,2,3,7], 
                  '머신러닝':[1,2,5,6], '블록체인' : [0,2,4,5],'파이썬' : [1,2,5,6]}
    with open('./book/data/{}.json'.format(word)) as f:
        key = f.read().encode('utf-8')
        data = json.loads(key)
        
    center = pd.read_csv('./book/data/{}_CENTER.csv'.format(word))
    df = pd.DataFrame(list(data.values()), index = data.keys())

    li = []
    for i in range(8):
        
        ccc = np.array(center.iloc[i, 1:])
        sim = df.ix[ df['label'] == i , :-2].dot(ccc)
        
        li.append(sim.nlargest(7))
        
        
    group_no = cluster_li[word]
    books = {}
    for book_q in li[group_no[0]].index:
        books[book_q] = df['link'][book_q]
    
    books1 = {}
    for book_w in li[group_no[1]].index:
        books1[book_w] = df['link'][book_w]
    
    books2 = {}
    for book_e in li[group_no[2]].index:
        books2[book_e] = df['link'][book_e]
    
    books3 = {}
    for book_r in li[group_no[3]].index:
        books3[book_r] = df['link'][book_r]

    return render(request, 'book/book_index.html', {'books' : books, 'books1': books1, 
                                                    'books2' : books2, 'books3' : books3})
                                                    
            
            