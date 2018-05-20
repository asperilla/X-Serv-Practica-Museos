from django.contrib import admin

# Register your models here.

from .models import Museo, Comentario, PagPersonal

admin.site.register(Museo)
admin.site.register(Comentario)
admin.site.register(PagPersonal)
