from django.db import models
from django.utils import timezone

class Empresas(models.Model):
    nome_empresa = models.CharField(max_length=100)

class Tecnicos(models.Model):
    nome_tecnico = models.CharField(max_length=100)

class Equipamentos(models.Model):
    tipo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)

class Saida(models.Model):
    empresa = models.CharField(max_length=100, default='valor_padrao')
    tecnico = models.CharField(max_length=100, default='valor_padrao')
    tipo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    numero_serie = models.CharField(max_length=100)
    quantidade = models.PositiveIntegerField()
    data_saida = models.DateField()
    obs = models.TextField()
    data_hora_atual = models.DateTimeField()
    ip_cliente = models.GenericIPAddressField()
    nome_usuario_windows = models.CharField(max_length=100)
    cupom = models.PositiveIntegerField()

class SaidaTemporaria(models.Model):
    empresa = models.CharField(max_length=100, default='valor_padrao')
    tecnico = models.CharField(max_length=100, default='valor_padrao')
    tipo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    numero_serie = models.CharField(max_length=100)
    quantidade = models.PositiveIntegerField()
    data_saida = models.DateField()
    obs = models.TextField()
    data_hora_atual = models.DateTimeField()
    ip_cliente = models.GenericIPAddressField()
    nome_usuario_windows = models.CharField(max_length=100)
    cupom = models.PositiveIntegerField()
    

class Entrega(models.Model):
    empresa = models.CharField(max_length=100, default='valor_padrao')
    tecnico = models.CharField(max_length=100, default='valor_padrao')
    tipo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    numero_serie = models.CharField(max_length=100)
    quantidade = models.PositiveIntegerField()
    data_entrega = models.DateField()
    obs = models.TextField()
    data_hora_atual = models.DateTimeField()
    ip_cliente = models.GenericIPAddressField()
    nome_usuario_windows = models.CharField(max_length=100)
    cupom = models.PositiveIntegerField()

class EntregaTemporaria(models.Model):
    empresa = models.CharField(max_length=100, default='valor_padrao')
    tecnico = models.CharField(max_length=100, default='valor_padrao')
    tipo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    numero_serie = models.CharField(max_length=100)
    quantidade = models.PositiveIntegerField()
    data_entrega = models.DateField()
    obs = models.TextField()
    data_hora_atual = models.DateTimeField()
    ip_cliente = models.GenericIPAddressField()
    nome_usuario_windows = models.CharField(max_length=100)
    cupom = models.PositiveIntegerField()