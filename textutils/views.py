#this file is  created by me;
from django .http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"index.html")

#analysing text
def analyze(request):
    input_text=request.POST.get("text","default")
    removepunc=request.POST.get("removepunc","off")
    fullcaps=request.POST.get("fullcaps","off")
    largest=request.POST.get("largest","off")
    smallest=request.POST.get("smallest","off")
    charcount=request.POST.get("charcount","off")

    if(removepunc=="on"):
        analyzed= ""
        punctuation='''!@#$%^&*()_+-=<>?:",./;'~'''
        for char in input_text:                                 #removing punctuations
            if(char not in punctuation):
                analyzed=analyzed+char
        params={"purpose":"Remove Punctuatios" , "analyzed_text":analyzed}
        return render(request,"analyze.html",params)

    elif(fullcaps=="on"):
        analyzed=""
        for char in input_text:
            analyzed=analyzed+char.upper()                                        #convert to fullcaps
        params={"purpose":"Change to uppercase" , "analyzed_text":analyzed}
        return render(request,"analyze.html",params)

    elif(largest=="on"):
        analyzed=""
        input_text_lst = input_text.split(" ")
        analyzed = input_text_lst[0]
        for word in input_text_lst:
            if(len(analyzed) < len(word)):
                analyzed = word
        params={"purpose":"Find the largest" , "analyzed_text":analyzed}
        return render(request,"analyze.html",params)

    elif(smallest=="on"):
        analyzed = ""
        input_text_lst = input_text.split(" ")
        analyzed = input_text_lst[0]
        for word in input_text_lst:
            if(len(analyzed) > len(word)):
                analyzed = word
        params={"purpose":"Find the largest" , "analyzed_text":analyzed}
        return render(request,"analyze.html",params)
  
    elif(charcount=="on"):
        analyzed=0
        for char in input_text:                                                        #counts the characters
            analyzed+=1
        params={"purpose":"Counts the character" , "analyzed_text":analyzed}
        return render(request,"analyze.html",params) 


    else:
        analyzed=input_text
        params={"purpose":"Counts the character" , "analyzed_text":analyzed}
        return render(request,"analyze.html",params) 