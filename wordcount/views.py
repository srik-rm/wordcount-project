from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']
    li = fulltext.split(" ")
    dic = {}
    for i in li:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    res = max(dic,key=dic.get)

    return render(request, 'count.html', {'fulltext': fulltext, 'count': res})

def about(request):
    return render(request, 'about.html')
