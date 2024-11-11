from django.shortcuts import render

def codeGenerator(request):
    return render(request,"generator/codeGenerator.html",{'headTitle' : 'Code Generator','toggle' : "true"})

def emailGenerator(request):
    return render(request,"generator/emailGenerator.html", {'headTitle' : 'Email Generator','toggle' : "true"})

def imageEditor(request):
    return render(request,"generator/imageEditor.html", {'headTitle' : 'Image Generator','toggle' : "true",'toggle' : "true"})

def imageGenerator(request):
    return render(request,"generator/imageGenerator.html", {'headTitle' : 'Image Generator','toggle' : "true"})

def textGenerator(request):
    return render(request,"generator/textGenerator.html",{'headTitle' : 'Text Generator','toggle' : "true"})

def vedioGenerator(request):
    return render(request,"generator/vedioGenerator.html", {'headTitle' : 'Vedio Generator','toggle' : "true"})
