from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from post.models import post
from post.forms import FormularioBuscarPosts

'''
d
'''
def ver_posts(request):
    posts = post.objects.all().order_by('id')
    return render(request, 'post/ver_posts.html', { 'posts' : posts })


def buscar_posts(request):
    titulo = request.GET.get('titulo', None)

    if titulo:
        posts = post.objects.filter(titulo__icontains=titulo)
    else:
        posts = post.objects.all()

    posts = posts.order_by('id')

    formulario_buscar_posts = FormularioBuscarPosts()

    return render(request, 'post/buscar_posts.html', { 'formulario_buscar_posts' : formulario_buscar_posts, 'posts' : posts })



class VerPostView(DetailView):
    model         = post
    template_name = 'post/ver_post.html'


class NuevoPostView(LoginRequiredMixin, CreateView):
    model = post
    template_name = 'post/nuevo_post.html'
    success_url = reverse_lazy('ver_posts')  
    fields = ['titulo', 'subtitulo', 'contenido', 'imagen']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class EditarPostView(LoginRequiredMixin, UpdateView):
    model         = post
    template_name = 'post/editar_post.html'
    success_url   = '/posts/'
    fields        = ['titulo', 'subtitulo', 'contenido', 'imagen']


class EliminarPostView(LoginRequiredMixin, DeleteView):
    model         = post
    template_name = 'post/borrar_post.html'
    success_url   = '/posts/'
