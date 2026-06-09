from django.shortcuts import render, redirect, get_object_or_404
from .forms import EtudiantForm
from .models import Etudiant


def ajouter_etudiant(request):

    if request.method == 'POST':
        form = EtudiantForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('ajouter')

    else:
        form = EtudiantForm()

    return render(request, 'etudiants/ajouter.html', {'form': form})


def modifier_etudiant(request, id):
    etudiant = get_object_or_404(Etudiant, id=id)

    if request.method == 'POST':
        form = EtudiantForm(request.POST, instance=etudiant)

        if form.is_valid():
            form.save()
            return redirect('liste_etudiants')

    else:
        form = EtudiantForm(instance=etudiant)

    return render(request, 'etudiants/ajouter.html', {'form': form})


def supprimer_etudiant(request, id):
    etudiant = get_object_or_404(Etudiant, id=id)
    etudiant.delete()
    return redirect('liste')


def dashboard(request):
    total_etudiants = Etudiant.objects.count()

    return render(request, 'etudiants/dashboard.html', {
        'total_etudiants': total_etudiants
    })


def liste_etudiants(request):
    etudiants = Etudiant.objects.all()
    return render(request, 'etudiants/liste.html', {
        'etudiants': etudiants
    })

def accueil(request):
    return render(request, 'etudiants/accueil.html')