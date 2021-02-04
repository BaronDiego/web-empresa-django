from django.urls import path
from . import views

urlpatterns = [
    path('<int:pagina_id>/<slug:pagina_titulo>/', views.pagina, name="pagina"),
]