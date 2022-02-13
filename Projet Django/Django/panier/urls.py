from django.urls import path
from . import views

urlpatterns = [
    path('panier',views.articles_in_panier, name='articles_in_panier')
]