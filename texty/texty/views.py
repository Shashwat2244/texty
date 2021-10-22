from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')
def analyze(request):
    djtext=request.POST.get('text','default')
    #CHeck Checkbox Value
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    spaceremover=request.POST.get('spaceremover','off')
    length=request.POST.get('Length','off')
    #Check which checkbox is on

    if removepunc=="on":
        analyzed=""
        punctuations='''!@#$%^&*()_-{}[];:'",><.?/\|'''
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Removed Punctuations',"analyzed_text":analyzed}
        return render(request,'analyze.html',params)
    elif (fullcaps=='on'):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={'purpose':'Change to Upper Case','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif(newlineremover == 'on'):
        analyzed = ""
        for char in djtext:
            if char !="\n":

                analyzed = analyzed + char
        params = {'purpose': 'Remove NEw Lines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif spaceremover=='on':
        analyzed=""
        for index,char in enumerate(djtext):
            if djtext[index] == " ":
                pass
            else:
                analyzed=analyzed+char
        params={'purpose': 'Extra Spaces Removed', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif length=='on':
        analyzed=""
        for index,char in enumerate(djtext):
            if djtext[index]==" ":
                pass
            else:
                analyzed=analyzed+char
        le=len(analyzed)
        params = {'purpose': 'Length of string', 'analyzed_text': le}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse('''Error''')