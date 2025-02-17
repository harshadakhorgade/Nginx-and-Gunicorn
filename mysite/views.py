from django.http import HttpResponse

from django.shortcuts import render

def index(request):
    params ={'name':'Harshada','place':'Gargantua'}
    return render(request,"home.html",params)

def about(request):
    return HttpResponse("<h1> about </h1>")

def analyze(request):

    djtext =request.POST.get('text','default')
    print(djtext)

    remove =request.POST.get('remove','off')
    print(remove)

    capitalize =request.POST.get('capitalize','off')
    print(capitalize)

    length =request.POST.get('length','off')
    print(length)

    if remove == "on":
        analyzed =""
        punctuation = ''' . , ? ! : ; ' " ( ) [ ] { } - – — … / \ @ # $ % ^ & * _ = + < > |'''

        for char in djtext:
            if char not in  punctuation :
                analyzed =analyzed+ char
            
            
        params ={'purpose':'remove punctuation','analyzed_text':analyzed}
        djtext =analyzed

    
        # return render(request,'analyze.html',params)
    

    if capitalize == 'on':
        analyzed =""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'capitalize', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        djtext =analyzed
    
    if length == 'on':
        analyzed =""
        count = sum(1 for char in djtext if char.isalpha())
            
        params = {'purpose': 'length', 'analyzed_text': count}
        djtext =analyzed

    
    return render(request, 'analyze.html', params)
        
        
    

   