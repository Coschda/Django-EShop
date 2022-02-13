from django.shortcuts import render
from .models import Article

# Create your views here.
def accueil(request):
  art = Article.objects.raw("SELECT * FROM articles_article ORDER BY note DESC LIMIT 5;")
  return render(request, 'home/accueil.html',{"home_articles":art})

def solart(request, id):
  art = Article.objects.get(id=id)
  return render(request,'articles/solart.html',{"art":art})

def articles(request):
  art = Article.objects.all()
  return render(request,'articles/articles.html', {"articles":art})