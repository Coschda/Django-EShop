from django.shortcuts import render
from articles.models import Article

# Create your views here.
# def panier(requests):
#   return render(requests, 'articles/panier.html')

def articles_in_panier(request):
  artp = Article.objects.all()
  return render(request,'articles/panier.html', {"artp":artp})