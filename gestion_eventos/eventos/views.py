from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .models import Evento, RegistroEvento
from django.contrib.auth.decorators import login_required

# Create your views here.
#crear eventos
class CrearEventoView(CreateView):
    model = Evento
    fields = ['nombre', 'descripcion', 'fecha', 'lugar', 'organizador']
    template_name = 'eventos/crear_evento.html'
    success_url = reverse_lazy('listar_eventos')

# registrar usuario en un evento
@login_required
def registrar_en_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    RegistroEvento.objects.get_or_create(usuario=request.user, evento=evento)
    return redirect('detalle_evento', evento_id=evento_id)

def lista_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos/lista_eventos.html', {'eventos': eventos})

def detalle_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    return render(request, 'eventos/detalle_evento.html', {'evento': evento})