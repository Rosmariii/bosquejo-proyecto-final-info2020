from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Producto, Rubro
from .forms import Formulario_Alta_Producto, Formulario_Alta_Rubro
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def Listar(request):
    productos = Producto.objects.all()
    ctx = {}
    ctx['p'] = productos
    return render(request,'productos/listar.html', ctx)

class Alta_Producto(LoginRequiredMixin, CreateView):
    model = 'Producto'
    form_class = Formulario_Alta_Producto
    template_name = 'productos/alta_producto.html'
    success_url = reverse_lazy('home')

class Alta_Rubro(CreateView):
    model = 'Rubro'
    form_class = Formulario_Alta_Rubro
    template_name = 'productos/alta_rubro.html'
    success_url = reverse_lazy('home')