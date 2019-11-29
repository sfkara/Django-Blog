from django.shortcuts import render, HttpResponse,redirect
from .forms import ArticleForm
from django.contrib import messages
# Create your views here.


def index(request):
    context = {
        "number1": 10,
        "number2": 20,
        "number3": 30
    }
    return render(request, "index.html", context)


def about(request):
    return render(request, "about.html")


def detail(request, id):
    return HttpResponse("Detail: " + str(id))

def dashboard(request):
    return render(request,"dashboard.html")

def addArticle(request):
    form = ArticleForm(request.POST or None)

    if form.is_valid():
        article = form.save(commit=False)
        article.author =request.user
        article.save()
        messages.success(request,"Makale Kaydedildi")
        return redirect("index")

    return render(request,"addarticle.html",{"form":form})    