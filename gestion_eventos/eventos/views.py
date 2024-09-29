from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .models import Evento, RegistroEvento
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.utils import timezone
from django import forms

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

#----
# mostrar información avanzada
def consultas_avanzadas(request):
    # usuarios que están registrados en un evento específico
    evento_id = request.GET.get('evento_id')
    if evento_id:
        usuarios_registrados = RegistroEvento.objects.filter(evento_id=evento_id).count()
    else:
        usuarios_registrados = None

    # eventos que se están llevando a cabo este mes
    fecha_actual = timezone.now()
    eventos_mes = Evento.objects.filter(fecha__month=fecha_actual.month, fecha__year=fecha_actual.year).count()

    # usuarios más activos en términos de participación en eventos?
    usuarios_activos = (
        RegistroEvento.objects.values('usuario')
        .annotate(participacion=Count('evento'))
        .order_by('-participacion')[:5]  # Los 5 usuarios más activos
    )

    # eventos organizados por un usuario en particular
    usuario_id = request.GET.get('usuario_id')
    if usuario_id:
        eventos_organizados = Evento.objects.filter(organizador_id=usuario_id).count()
    else:
        eventos_organizados = None

    context = {
        'usuarios_registrados': usuarios_registrados,
        'eventos_mes': eventos_mes,
        'usuarios_activos': usuarios_activos,
        'eventos_organizados': eventos_organizados,
    }

    return render(request, 'eventos/consultas_avanzadas.html', context)


class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nombre', 'descripcion', 'fecha', 'lugar', 'organizador']  # Campos a editar


def editar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)

    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('detalle_evento', evento_id=evento.id)  # Redirige a la página de detalles del evento editado
    else:
        form = EventoForm(instance=evento)

    return render(request, 'eventos/editar_evento.html', {'form': form, 'evento': evento})

def eliminar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)

    if request.method == 'POST':
        evento.delete()
        return redirect('listar_eventos')

    return render(request, 'eventos/eliminar_evento.html', {'evento': evento})