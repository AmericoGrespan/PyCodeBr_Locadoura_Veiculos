from django.shortcuts import get_object_or_404, redirect, render
from django.views import View  # pra usar a classe Views Base
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from cars.forms import frm_categoria_origem, frm_perfil_cliente, frmcarro, frmCicloVida
from cars.models import tbl_carro, tbl_perfil_cliente

from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# ====================================================================#
# Views - Categoria de Origem
# ====================================================================#


class categorianova(View):

    def get(self, request):
        categorianova = (
            frm_categoria_origem()
        )  # Instancia o formulário vazio para o GET
        return render(
            request, "frm_cad_categoria.html", {"categorianova": categorianova}
        )

    def post(self, request):
        categorianova = frm_categoria_origem(request.POST)
        if categorianova.is_valid():
            categorianova.save()
            return redirect("categoria_origem")
        return render(
            request, "frm_cad_categoria.html", {" categorianova ": categorianova}
        )


###################################################################
# ====================================================================#
# Views - Cars
# ====================================================================#
@method_decorator(login_required(login_url="login"), name="dispatch")
class NewCarCreateView(CreateView):
    model = tbl_carro
    form_class = frmcarro
    template_name = "new_car.html"
    context_object_name = "tbl_carros"
    success_url = "/cars/"


class CarsDetailView(DetailView):
    model = tbl_carro
    # form_class          =
    template_name = "car_detail.html"
    # context_object_name = 'tbl_carros'


@method_decorator(login_required(login_url="login"), name="dispatch")
class CarsUpdateView(UpdateView):
    model = tbl_carro
    form_class = frmcarro
    template_name = "car_update.html"
    success_url = "/cars/"


# ====================================================================#
# Generica View - ListViews
# tbl_carros = tbl_carro.filter(model_icontains=search) # Busca o que tem no campo digitado nao importa caixa alta ou baixa
# tbl_carros = tbl_carro.objects.Filter(model_contains=serche) # Busca a palavra executa digitada
# tbl_carros = tbl_carro.objects.filter(brand__brand='Fiat') # filtra pelo codigo da modelo do carro
# tbl_carros = tbl_carro.objects.filter(brand=7) # filtra pelo codigo da modelo do carro
# tbl_carros = tbl_carro.objects.filter(model='Duster')
# tbl_carros  = tbl_carro.objects.filter(model__contains='t')

# ====================================================================#


class CarsListViews(ListView):

    model = tbl_carro
    template_name = "cars.html"
    context_object_name = "tbl_carros"

    def get_queryset(self):
        tbl_carros = super().get_queryset().order_by("model")
        search = self.request.GET.get("search")
        if search:
            tbl_carros = tbl_carros.filter(model__icontains=search)
        return tbl_carros


# ====================================================================#
# classe para deletar


@method_decorator(login_required(login_url="login"), name="dispatch")
class CarDeleteView(DeleteView):
    model = tbl_carro
    template_name = "car_delete.html"  # Corrigido para 'car_delete.html'
    success_url = "/cars/"


###################################################################
# ====================================================================#
# VIEWS  DO CICLO DE VIDA (Usando ModelForm)
# ====================================================================#


@method_decorator(login_required(login_url="login"), name="dispatch")
def inc_ciclo_vida(request):
    if request.method == "POST":
        inc_ciclo_vida = frmCicloVida(request.POST)
        if inc_ciclo_vida.is_valid():
            inc_ciclo_vida.save()
        return redirect("inc_ciclo_vida")
    else:
        inc_ciclo_vida = frmCicloVida()

    return render(request, "frm_ciclo_vida.html", {"inc_ciclo_vida": inc_ciclo_vida})


# ====================================================================#
# VIEWS  DO perfil de cliente  (Usando ModelForm)
# ====================================================================#
# 1. CONSULTA / LISTAGEM (Com barra de pesquisa)
def list_perfil_cliente(request):
    perfis = tbl_perfil_cliente.objects.all().order_by("perfil_cliente")

    # Sistema de busca por nome do perfil
    search = request.GET.get("search")
    if search:
        perfis = perfis.filter(perfil_cliente__icontains=search)

    return render(request, "lista_perfil_cliente.html", {"perfis": perfis})


# 2. INCLUSÃO (Sua view atual, levemente ajustada no redirect)
@method_decorator(login_required(login_url="login"), name="dispatch")
def inc_perfil_cliente(request):
    if request.method == "POST":
        inc_perfil_cliente = frm_perfil_cliente(request.POST)
        if inc_perfil_cliente.is_valid():
            inc_perfil_cliente.save()
    else:
        inc_perfil_cliente = frm_perfil_cliente()

    return render(
        request,
        "frm_crud_perfil_cliente.html",
        {"inc_perfil_cliente": inc_perfil_cliente},
    )


# 3. EDIÇÃO (Reutiliza o formulário existente!)
def edit_perfil_cliente(request, pk):
    # Busca o perfil pelo ID (pk) ou retorna erro 404 se não existir
    perfil = get_object_or_404(tbl_perfil_cliente, pk=pk)

    if request.method == "POST":
        # Passamos o 'instance=perfil' para o Django saber que estamos atualizando um registro existente, e não criando um novo
        form = frm_perfil_cliente(request.POST, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect("list_perfil_cliente")
    else:
        # Carrega o formulário já preenchido com os dados do banco
        form = frm_perfil_cliente(instance=perfil)

    return render(
        request,
        "frm_crud_perfil_cliente.html",
        {"inc_perfil_cliente": form, "titulo": "Editar Perfil"},
    )


# 4. EXCLUSÃO (Simples e direta)
@method_decorator(login_required(login_url="login"), name="dispatch")
def delete_perfil_cliente(request, pk):
    perfil = get_object_or_404(tbl_perfil_cliente, pk=pk)
    if request.method == "POST":
        perfil.delete()
        return redirect("list_perfil_cliente")

    # Retorna uma página de confirmação simples de exclusão
    return render(request, "confirm_delete.html", {"perfil": perfil})


def register_view(request):

    return
