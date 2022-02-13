from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from .models import Mails
from django.contrib import messages
import re

# Create your views here.
def inscrire(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        passw = request.POST['password']
        passw2 = request.POST['password2']

        if username=="" or email=="" or passw=="" or passw2=="":
            messages.info(request, 'Veuillez remplir tous les champs.')
            return redirect('inscrire')

        elif passw != passw2:
            messages.info(request, 'Les mots de passe ne sont pas les mêmes.')
            return redirect('inscrire')

        elif User.objects.filter(username=username).exists():
            messages.info(request, "Nom d'utilisateur déjà prit.")
            return redirect('inscrire')
            
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email déjà utilisé.')
            return redirect('inscrire')
            
        else:
            user = User.objects.create_user(username=username, email=email, password=passw)
            user.save();
            return redirect('connexion')

    else:
        return render(request, 'connexion/register.html')

def connexion(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'Compte invalide.')
            return redirect("connexion")
    else:
        return render(request, 'connexion/connexion.html')

def deconnexion(request):
    auth.logout(request)
    return redirect('/')

def newsletter(request):
    regex = r'/([^\w!\&+@-Z.]+)/'
    if request.method=="POST":
        if re.search(regex, request.POST["mairu"]) != None:
            return redirect('/')
        else:
            return redirect('connexion')
    else:
        return redirect('/')