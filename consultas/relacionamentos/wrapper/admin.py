from django.contrib import admin
from wrapper.models import Cidade, Esporte, Time, Pessoa

# Register your models here.
admin.site.register((Cidade, Esporte, Time, Pessoa))