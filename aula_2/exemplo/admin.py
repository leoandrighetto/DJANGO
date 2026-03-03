from django.contrib import admin
from exemplo.models import Categoria
from exemplo.models import Disciplina
from exemplo.models import Compra

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Disciplina)
admin.site.register(Compra)