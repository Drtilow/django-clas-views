from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='staticka.html'), name='home'),
    path('zobraz/', views.zobraz_parametr, name='zobraz_parametr'),
    path('kategorie/', views.vyber_kategorii, name='vyber_kategorie'),
    path('zpetna_vazba/', views.zpetna_vazba, name='zpetna_vazba'),
    path('staticka/', TemplateView.as_view(template_name='staticka.html'), name='staticka'),
    path('kontakt/', views.KontaktView.as_view(), name='kontakt'),
]