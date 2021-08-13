# I HAVE CREATED THIS FILE - VIKAS

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        params = {'purpose': 'removed punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if fullcaps == 'on':
        analyzed = ''
        for char in djtext:
            analyzed += char.upper()
        params = {'purpose': 'change it to UPPERCASE', 'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremover == 'on':
        analyzed = ''
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed += char
        params = {'purpose': 'New Line Remover', 'analyzed_text': analyzed}
        djtext = analyzed

    if extraspaceremover == 'on':
        analyzed = ''
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed += char
        params = {'purpose': 'Extra Space Remover', 'analyzed_text': analyzed}

    if fullcaps != 'on' and removepunc != "on" and newlineremover != 'on' and extraspaceremover != 'on':
        return HttpResponse("error")

    return render(request, 'analyze.html', params)

