from django.shortcuts import render
from .models import Texto

# Create your views here.
# resumo/views.py

def inserir_texto(request):
    if request.method == 'POST':
        texto_completo = request.POST['texto_completo']
        # Resumir o texto aqui (usando uma biblioteca de resumo automático)
        resumo_automatico = "Resumo automático do texto"
        texto = Texto.objects.create(texto_completo=texto_completo, resumo_automatico=resumo_automatico)
        return render(request, 'resumo/inserir_texto.html', {'texto': texto})
    else:
        return render(request, 'resumo/inserir_texto.html')

def gerar_resumo(request, texto_id):
    texto = Texto.objects.get(id=texto_id)
    return render(request, 'resumo/gerar_resumo.html', {'texto': texto})

