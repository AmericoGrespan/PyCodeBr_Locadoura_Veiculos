""" """

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path

from accounts.views import login_view, register_view
from cars.views import (
    CarsDetailView,
    CarsListViews,
    CarsUpdateView,
    NewCarCreateView,
    categorianova,
    delete_perfil_cliente,
    edit_perfil_cliente,
    inc_ciclo_vida,
    inc_perfil_cliente,
    list_perfil_cliente,
    CarDeleteView,
)

urlpatterns = [
    path("", CarsListViews.as_view(), name="cars_list"),
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("admin/", admin.site.urls),
    path("cars/", CarsListViews.as_view(), name="cars_list"),
    path("car/<int:pk>/", CarsDetailView.as_view(), name="car_detail"),
    path("car/<int:pk>/update/", CarsUpdateView.as_view(), name="car_update"),
    # Linha 32 corrigida:
    path("car/<int:pk>/delete/", CarDeleteView.as_view(), name="car_delete"),
    path("new_car/", NewCarCreateView.as_view(), name="new_car"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("ciclovida/", inc_ciclo_vida, name="ciclo_vida"),
    path("perfilcliente/", inc_perfil_cliente, name="perfil_cliente"),
    path("perfis/", list_perfil_cliente, name="list_perfil_cliente"),
    path("perfis/novo/", inc_perfil_cliente, name="inc_perfil_cliente"),
    path("perfis/editar/<int:pk>/", edit_perfil_cliente, name="edit_perfil_cliente"),
    path(
        "perfis/excluir/<int:pk>/", delete_perfil_cliente, name="delete_perfil_cliente"
    ),
    path("categoria_origem/", categorianova.as_view(), name="categoria_origem"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
