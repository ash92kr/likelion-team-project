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
        
    center = pd.read_csv('./book/{}_CENTER.csv'.format(word))
    df = pd.DataFrame(list(data.values()), index = data.keys())
    
    li = []
    for i in range(8):
        
        ccc = np.array(center.iloc[i,1:])
        sim = df.ix[ df['label'] == i , :-2].dot(ccc)
        
        li.append(sim.nlargest(7))
    books = {}
    for book_q in li[0].index:
        books[book_q] = df['link'][book_q]

    books1 = {}
    for book_w in li[4].index:
        books1[book_w] = df['link'][book_w]

    books2 = {}
    for book_e in li[2].index:
        books2[book_e] = df['link'][book_e]

    books3 = {}
    for book_r in li[5].index:
        books3[book_r] = df['link'][book_r]

    return render(request, 'book/book_index.html', {'books' : books, 'books1': books1, 'books2' : books2, 'books3' : books3})
    
# css 파일을 바꾸고 난 다음에는 ctrl+shift+R을 통해서 강력 새로고침을 해야 바뀐 스타일이 적용됨 