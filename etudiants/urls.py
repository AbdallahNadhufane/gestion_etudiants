from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns =[
    path('', views.accueil, name='accueil'),

    path(
    'login/',
    auth_views.LoginView.as_view(
        template_name='etudiants/login.html'
    ),
    name='login'
    ),

    path(
    'logout/',
    auth_views.LogoutView.as_view(),
    name='logout'
    ),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('ajouter/', views.ajouter_etudiant, name = 'ajouter'),
    path('etudiants/', views.liste_etudiants, name='liste'),
    path('modifier/<int:id>/', views.modifier_etudiant, name='modifier'),
    path('supprimer/<int:id>/', views.supprimer_etudiant, name='supprimer'),
]