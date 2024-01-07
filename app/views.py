from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

from .forms import ProductForm
from .models import Product, Order


# Create your views here.

class GetPosts(ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'products'


class GetDetailView(DetailView):
    model = Product
    template_name = 'post_detail.html'
    context_object_name = 'object'


class CreatePost(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'post_form.html'
    success_url = '/'

class UpdatePost(UpdateView):
    model = Product
    fields = '__all__'
    template_name = 'post_form.html'

    success_url = '/'

class DeletePost(DeleteView):
    model = Product
    success_url = '/'
    template_name = 'confirm_delete.html'


class AddToCart(CreateView):
    model = Order
    fields = '__all__'
    template_name = 'add_to_cart.html'
    success_url = '/'

class GetOrders(ListView):
    model = Order
    context_object_name = 'orders'
    template_name = 'my_orders.html'

class DeleteOrder(DeleteView):
    model = Order
    success_url = '/orders'
    template_name = 'confirm_delete.html'