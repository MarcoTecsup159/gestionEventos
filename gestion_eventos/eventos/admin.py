from django.contrib import admin
from .models import Evento, RegistroEvento

# Register your models here.
admin.site.register(Evento)
admin.site.register(RegistroEvento)