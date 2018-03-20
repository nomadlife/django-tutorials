from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenicate, login
from django.views import generic
from django.views.generic import View
from .models import Album
from .forms import UserForm


class IndexView(generic.ListView):
    template_name = 'music/index.html'

    def get_queryset(serl):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title','genre','album_logo']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title','genre','album_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')

class UserFormView(view):
    form_class = UserForm
    template_name = 'music/registration_form.html'

    def get(self, request):
