from django.urls import path
from . import views

urlpatterns = [
    path('inserir_texto/', views.inserir_texto, name='inserir_texto'),
    path('gerar_resumo/<int:texto_id>/', views.gerar_resumo, name='gerar_resumo'),
]
