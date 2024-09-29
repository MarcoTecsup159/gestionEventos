
from django.urls import path
from .views import CrearEventoView, registrar_en_evento, lista_eventos, detalle_evento, consultas_avanzadas, editar_evento, eliminar_evento

urlpatterns = [
    path('crear/', CrearEventoView.as_view(), name='crear_evento'),
    path('registrar/<int:evento_id>/', registrar_en_evento, name='registrar_evento'),
    path('', lista_eventos, name='listar_eventos'),
    path('<int:evento_id>/', detalle_evento, name='detalle_evento'),
    path('consultas/', consultas_avanzadas, name='consultas_avanzadas'),
    path('editar/<int:evento_id>/', editar_evento, name='editar_evento'),
    path('eliminar/<int:evento_id>/', eliminar_evento, name='eliminar_evento'),
]
