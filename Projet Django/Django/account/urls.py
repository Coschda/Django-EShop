from django.urls import path
from . import views

urlpatterns = [
    path('inscrire', views.inscrire, name="inscrire"),
    path('connexion', views.connexion, name="connexion"),
    path('deconnexion', views.deconnexion, name="logout"),
    path('newsletter', views.newsletter, name="newsletter")
]