from django.urls import path
from . import views

urlpatterns = [
    path('',views.accueil, name='accueil'),
    path('articles',views.articles),
    path("articles/<int:id>", views.solart)
]