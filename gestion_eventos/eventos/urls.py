
from django.urls import path
from .views import CrearEventoView, registrar_en_evento, lista_eventos, detalle_evento, consultas_avanzadas

urlpatterns = [
    path('crear/', CrearEventoView.as_view(), name='crear_evento'),  # Ruta para crear un nuevo evento
    path('registrar/<int:evento_id>/', registrar_en_evento, name='registrar_evento'),  # Ruta para registrar usuario en un evento
    path('', lista_eventos, name='listar_eventos'),
    path('<int:evento_id>/', detalle_evento, name='detalle_evento'),
    path('consultas/', consultas_avanzadas, name='consultas_avanzadas'),
]
