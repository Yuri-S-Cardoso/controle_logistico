from django.shortcuts import render, redirect
from .models import Empresas, Tecnicos, Equipamentos, Saida, Entrega, SaidaTemporaria, EntregaTemporaria
import socket, os, datetime
from datetime import date
from django.utils import timezone
from django.views.generic import ListView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.http import JsonResponse
import random
from django.db.models import Q


def index(request):
    return render(request, 'pages/index.html')

def saida(request):
    saida_temporaria = None
    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'salvar':            
            empresa = request.POST.get('empresa')
            tecnico = request.POST.get('tecnico')
            tipo = request.POST.get('tipo')
            marca = request.POST.get('marca')
            modelo = request.POST.get('modelo')
            numero_serie = request.POST.get('numero_serie')
            quantidade = request.POST.get('quantidade')
            data_saida_str = request.POST.get('data_saida')
            data_saida = datetime.datetime.strptime(data_saida_str, '%Y-%m-%d').date()
            obs = request.POST.get('obs')
            data_hora_atual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            client_ip = get_client_ip(request)
            windows_username = os.getlogin()
            cupom = request.POST.get('cupom')

            saidas_temporarias = SaidaTemporaria(
                empresa=empresa,
                tecnico=tecnico,
                tipo=tipo,
                marca=marca,
                modelo=modelo,
                numero_serie=numero_serie,
                quantidade=quantidade,
                data_saida=data_saida,
                obs=obs,
                data_hora_atual=data_hora_atual,
                ip_cliente=client_ip,
                nome_usuario_windows=windows_username,
                cupom=cupom,
            )
            saidas_temporarias.save()

            tipos_equipamentos = Equipamentos.objects.values_list('tipo', flat=True).distinct()
            marcas_equipamentos = Equipamentos.objects.values_list('marca', flat=True).distinct()
            modelos_equipamentos = Equipamentos.objects.values_list('modelo', flat=True).distinct()
            empresas = Empresas.objects.all()
            tecnicos = Tecnicos.objects.all()
            contexto = {
                'tipos_equipamentos': tipos_equipamentos,
                'marcas_equipamentos': marcas_equipamentos,
                'modelos_equipamentos': modelos_equipamentos,
                'empresas': empresas,
                'tecnicos': tecnicos,
                'saida_temporaria': saida_temporaria,
            }
            return render(request, 'pages/saida.html', contexto)

        elif action == 'finalizar':            
            saidas_temporarias = SaidaTemporaria.objects.all()
            for saida_temporaria in saidas_temporarias:
                saida_permanente = Saida(
                    empresa=saida_temporaria.empresa,
                    tecnico=saida_temporaria.tecnico,
                    tipo=saida_temporaria.tipo,
                    marca=saida_temporaria.marca,
                    modelo=saida_temporaria.modelo,
                    numero_serie=saida_temporaria.numero_serie,
                    quantidade=saida_temporaria.quantidade,
                    data_saida=saida_temporaria.data_saida,
                    obs=saida_temporaria.obs,
                    data_hora_atual=saida_temporaria.data_hora_atual,
                    ip_cliente=saida_temporaria.ip_cliente,
                    nome_usuario_windows=saida_temporaria.nome_usuario_windows,
                    cupom=saida_temporaria.cupom,
                )
                saida_permanente.save()            
           
            saidas_temporarias.delete()

        return redirect('relatorio_saida')
    
    tipos_equipamentos = Equipamentos.objects.values_list('tipo', flat=True).distinct()
    marcas_equipamentos = Equipamentos.objects.values_list('marca', flat=True).distinct()
    modelos_equipamentos = Equipamentos.objects.values_list('modelo', flat=True).distinct()
    empresas = Empresas.objects.all()
    tecnicos = Tecnicos.objects.all()
    contexto = {
        'tipos_equipamentos': tipos_equipamentos,
        'marcas_equipamentos': marcas_equipamentos,
        'modelos_equipamentos': modelos_equipamentos,
        'empresas': empresas,
        'tecnicos': tecnicos,
        'saida_temporaria': saida_temporaria,
    }
    return render(request, 'pages/saida.html', contexto)

def entrega(request):
    entrega_temporaria = None
    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'salvar':            
            empresa = request.POST.get('empresa')
            tecnico = request.POST.get('tecnico')
            tipo = request.POST.get('tipo')
            marca = request.POST.get('marca')
            modelo = request.POST.get('modelo')
            numero_serie = request.POST.get('numero_serie')
            quantidade = request.POST.get('quantidade')
            data_entrega_str = request.POST.get('data_entrega')
            data_entrega = datetime.datetime.strptime(data_entrega_str, '%Y-%m-%d').date()
            obs = request.POST.get('obs')
            data_hora_atual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            client_ip = get_client_ip(request)
            windows_username = os.getlogin()
            cupom = request.POST.get('cupom')

            entregas_temporarias = EntregaTemporaria(
                empresa=empresa,
                tecnico=tecnico,
                tipo=tipo,
                marca=marca,
                modelo=modelo,
                numero_serie=numero_serie,
                quantidade=quantidade,
                data_entrega=data_entrega,
                obs=obs,
                data_hora_atual=data_hora_atual,
                ip_cliente=client_ip,
                nome_usuario_windows=windows_username,
                cupom=cupom,
            )
            entregas_temporarias.save()

            tipos_equipamentos = Equipamentos.objects.values_list('tipo', flat=True).distinct()
            marcas_equipamentos = Equipamentos.objects.values_list('marca', flat=True).distinct()
            modelos_equipamentos = Equipamentos.objects.values_list('modelo', flat=True).distinct()
            empresas = Empresas.objects.all()
            tecnicos = Tecnicos.objects.all()
            contexto = {
                'tipos_equipamentos': tipos_equipamentos,
                'marcas_equipamentos': marcas_equipamentos,
                'modelos_equipamentos': modelos_equipamentos,
                'empresas': empresas,
                'tecnicos': tecnicos,
                'entrega_temporaria': entrega_temporaria,
            }
            return render(request, 'pages/entrega.html', contexto)

        elif action == 'finalizar':            
            entregas_temporarias = EntregaTemporaria.objects.all()
            for entrega_temporaria in entregas_temporarias:
                entrega_permanente = Entrega(
                    empresa=entrega_temporaria.empresa,
                    tecnico=entrega_temporaria.tecnico,
                    tipo=entrega_temporaria.tipo,
                    marca=entrega_temporaria.marca,
                    modelo=entrega_temporaria.modelo,
                    numero_serie=entrega_temporaria.numero_serie,
                    quantidade=entrega_temporaria.quantidade,
                    data_entrega=entrega_temporaria.data_entrega,
                    obs=entrega_temporaria.obs,
                    data_hora_atual=entrega_temporaria.data_hora_atual,
                    ip_cliente=entrega_temporaria.ip_cliente,
                    nome_usuario_windows=entrega_temporaria.nome_usuario_windows,
                    cupom=entrega_temporaria.cupom,
                )
                entrega_permanente.save()            
           
            entregas_temporarias.delete()

        return redirect('relatorio_entrega')
    
    tipos_equipamentos = Equipamentos.objects.values_list('tipo', flat=True).distinct()
    marcas_equipamentos = Equipamentos.objects.values_list('marca', flat=True).distinct()
    modelos_equipamentos = Equipamentos.objects.values_list('modelo', flat=True).distinct()
    empresas = Empresas.objects.all()
    tecnicos = Tecnicos.objects.all()
    contexto = {
        'tipos_equipamentos': tipos_equipamentos,
        'marcas_equipamentos': marcas_equipamentos,
        'modelos_equipamentos': modelos_equipamentos,
        'empresas': empresas,
        'tecnicos': tecnicos,
        'entrega_temporaria': entrega_temporaria,
    }
    return render(request, 'pages/entrega.html', contexto)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_windows_username():
    return os.getlogin()

def relatorio(request):
    return render(request, 'pages/relatorio.html')

def empresa(request):
    if request.method == 'POST':
        nome_empresa = request.POST.get('nome_empresa')

        empresa = Empresas(
            nome_empresa=nome_empresa,
        )
        empresa.save()

        return redirect('index')

    return render(request, 'pages/empresa.html')

def tecnico(request):
    if request.method == 'POST':
        nome_tecnico = request.POST.get('nome_tecnico')

        tecnico = Tecnicos(
            nome_tecnico=nome_tecnico,
        )
        tecnico.save()

        return redirect('index')
    return render(request, 'pages/tecnico.html')

def equipamento(request):
    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        marca = request.POST.get('marca')
        modelo = request.POST.get('modelo')

        equipamento = Equipamentos(
            tipo=tipo,
            marca=marca,
            modelo=modelo,
        )
        equipamento.save()

        return redirect('index')
    return render(request, 'pages/equipamento.html')

def autorizacao(request):
    return render(request, 'pages/autorizacao.html')

def relatorio_saida(request):
    cupom = request.GET.get('cupom')
    if cupom:
        saidas = Saida.objects.filter(cupom=cupom)
        if saidas.exists():
            autorizacao = f"Autorizo a empresa {saidas[0].empresa} e o técnico {saidas[0].tecnico} a sair com os equipamentos abaixo para reparo."
        else:
            autorizacao = None
    else:
        saidas = []
        autorizacao = None
    return render(request, 'pages/relatorio_saida.html', {'saidas': saidas, 'autorizacao': autorizacao})

def relatorio_entrega(request):
    cupom = request.GET.get('cupom')
    if cupom:
        entregas = Entrega.objects.filter(cupom=cupom)
        if entregas.exists():
            autorizacao = f"Autorizo a empresa {entregas[0].empresa} e o técnico {entregas[0].tecnico} a sair com os equipamentos abaixo para reparo."
        else:
            autorizacao = None
    else:
        entregas = []
        autorizacao = None
    return render(request, 'pages/relatorio_entrega.html', {'entregas': entregas, 'autorizacao': autorizacao})

def senha(request):
    return render(request, 'pages/senha.html')

def rel_saida_total(request):
    data_inicio_str = request.GET.get('data_inicio')
    data_termino_str = request.GET.get('data_termino')

    saidas = Saida.objects.all()

    if data_inicio_str and data_termino_str:
        data_inicio = datetime.datetime.strptime(data_inicio_str, '%Y-%m-%d')
        data_termino = datetime.datetime.strptime(data_termino_str, '%Y-%m-%d') + datetime.timedelta(hours=23, minutes=59, seconds=59)
        
        saidas = saidas.filter(
            Q(data_hora_atual__gte=data_inicio) & Q(data_hora_atual__lte=data_termino)
        )
    
    context = {'saidas': saidas}
    return render(request, 'pages/rel_saida_total.html', context)

def rel_entrega_total(request):
    data_inicio_str = request.GET.get('data_inicio')
    data_termino_str = request.GET.get('data_termino')

    entregas = Entrega.objects.all()

    if data_inicio_str and data_termino_str:
        data_inicio = datetime.datetime.strptime(data_inicio_str, '%Y-%m-%d')
        data_termino = datetime.datetime.strptime(data_termino_str, '%Y-%m-%d') + datetime.timedelta(hours=23, minutes=59, seconds=59)
        
        entregas = entregas.filter(
            Q(data_hora_atual__gte=data_inicio) & Q(data_hora_atual__lte=data_termino)
        )
    
    context = {'entregas': entregas}
    return render(request, 'pages/rel_entrega_total.html', context)

def verificar_cupom_saida(request):
    cupom = request.GET.get('cupom')
    cupom_exists = Saida.objects.filter(cupom=cupom).exists()
    
    if cupom_exists:
        # Se o cupom existe, encontre o próximo cupom disponível
        ultimo_cupom = Saida.objects.latest('cupom')
        proximo_cupom = ultimo_cupom.cupom + 1
    else:
        # Se o cupom não existe, use o valor fornecido
        proximo_cupom = int(cupom)

    return JsonResponse({'proximo_cupom': proximo_cupom})

def verificar_cupom_entrega(request):
    cupom = request.GET.get('cupom')
    cupom_exists = Entrega.objects.filter(cupom=cupom).exists()

    if cupom_exists:
        # Se o cupom existe, encontre o próximo cupom disponível
        ultimo_cupom = Entrega.objects.latest('cupom')
        proximo_cupom = ultimo_cupom.cupom + 1
    else:
        # Se o cupom não existe, use o valor fornecido
        proximo_cupom = int(cupom)

    return JsonResponse({'proximo_cupom': proximo_cupom})
