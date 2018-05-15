from django.contrib import admin

# Register your models here.

from .models import Museo, Comentario

admin.site.register(Museo)
admin.site.register(Comentario)
