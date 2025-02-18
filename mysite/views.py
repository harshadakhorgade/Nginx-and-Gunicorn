from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name': 'Harshada', 'place': 'Gargantua'}
    return render(request, "home.html", params)

def about(request):
    return HttpResponse("<h1> About Page </h1>")

from django.http import HttpResponse
from django.shortcuts import render

def analyze(request):
    djtext = request.POST.get('text', 'default')
    remove = request.POST.get('remove', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    length = request.POST.get('length', 'off')

    analyzed = djtext  # ✅ Always initialize `analyzed` to avoid errors

    if remove == "on":
        punctuation = '''.,?!:;'\"()[]{}-–—…/\@#$%^&*_+=<>|'''
        analyzed = "".join(char for char in djtext if char not in punctuation)
    
    if capitalize == 'on':
        analyzed = analyzed.upper()  # ✅ Use `analyzed` instead of `djtext`

    if length == 'on':
        analyzed = len(analyzed)  # ✅ Use `analyzed`, not `djtext`

    # Ensure at least one option was selected
    if remove == 'off' and capitalize == 'off' and length == 'off':
        return HttpResponse("<h2>Please select at least one option!</h2>")

    return render(request, 'analyze.html', {'analyzed_text': analyzed})
